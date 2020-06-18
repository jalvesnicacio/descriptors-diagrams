from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server

class Service():

    def __init__(self, service_name, image_name, container_name, volumes, depends_on):
        #self.m_service_name = servc;
        #tem propriedade image? se sim, nomeie m_image_name
        self.__service_name = service_name
        self.__image_name = image_name
        self.__container_name = container_name
        self.__volumes = volumes
        self.__depends_on = depends_on
        #self.node = service_name

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    @property
    def service_name(self):
        return self.__service_name

    @property
    def depends_on(self):
        return self.__depends_on

    @property
    def volumes(self):
        return self.__volumes

    def design(self):
        with Cluster("service " + self.__service_name):
            img = Server(self.__image_name)
            self.node = img

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, img):
        self.__node = img
