
from diagram_builder import DiagramBuilder
import yaml

#load yaml file
stream = open('docker-compose-files/docker-compose-mysql.yaml')
data = yaml.load(stream, Loader=yaml.FullLoader)


#Criando o objeto Diagram (usando Builder pattern):
diagram = (
    DiagramBuilder(data)
    .with_title()
    .with_services()
    .with_volumes()
    .with_networks()
    .build()
    )

#Projetando o diagrama:
diagram.design("./diagram")
#self.__diagram_filename =
