from diagrams import Cluster, Diagram as DaC, Edge
from service import Service
from diagrams.k8s.storage import Volume



class Diagram():
    def __init__(self, title, services, volumes, networks):
        self.__title = title
        self.__services = services
        self.__volumes = volumes
        self.__networks = networks
        self.__dependencies = self.map_dependencies()


    def service_by_name(self, name):
        for s in self.__services:
            if(s.service_name == name):
                return s
        return None

    def design(self):
        with DaC(self.__title, filename="./diagram", show=False, direction="LR"):
            for s in self.__services:
                s.design()
            self.design_edges()
            self.design_volumes()


    def map_dependencies(self):
        dependencies_list = []
        for s in self.__services:
            for don in s.depends_on:
                dependencies_list.append((s.service_name,don))
        return dependencies_list

    #criando as ligações entre os serviços, dependendo da relação
    # de dependência entre eles: srv1 >> srv2
    def design_edges(self):
        for dep in self.__dependencies:
             node0 = self.service_by_name(dep[0]).node
             node1 = self.service_by_name(dep[1]).node
             node0 >> node1

        # self.service_by_name('api').node << self.service_by_name('web').node
        # self.service_by_name('web').node >> self.service_by_name('db').node
        # self.service_by_name('api').node >> self.service_by_name('db').node

    def design_volumes(self):
        services_volumes = []
        dashed_edge = Edge(color="darkgreen", style="dashed")
        for s in self.__services:
            for v in s.volumes:
                #vol = v.split(":")
                services_volumes.append((s.service_name,v))
        for sv in services_volumes:
             v = Volume(sv[1])
             v >> dashed_edge << self.service_by_name(sv[0]).node
