from diagram_builder import DiagramBuilder
import yaml

class DiagramController():

    def __init__(self):
        self.__diagram_filename = "./diagram"

    def build_diagram(self, filename):
        #load yaml file
        stream = open(filename)
        data = yaml.load(stream, Loader=yaml.FullLoader)
        #Criando o objeto Diagram:
        diagram = (
            DiagramBuilder(data)
            .with_title()
            .with_services()
            .with_volumes()
            .with_networks()
            .build()
            )
        #Projetando o diagrama:
        diagram.design(self.__diagram_filename)
        return self.__diagram_filename + ".png"
