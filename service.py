from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server

class Service():
    m_service_name = ""
    m_image_name = "image name"

    def __init__(self, servc, dict):
        self.m_service_name = servc;
        #tem propriedade image? se sim, nomeie m_image_name
        if(dict.get('image') is not None):
            self.m_image_name = dict.get('image')
        elif(dict.get('build') is not None):
            build = dict.get('build')
            if(build.get('container_name') is not None):
                self.m_image_name = build.get('container_name')
            else:
                self.m_image_name = build


    def design(self):
        with Cluster("service " + self.m_service_name):
            img = Server(self.m_image_name)
