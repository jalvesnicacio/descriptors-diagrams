
from diagram_builder import DiagramBuilder
import yaml

#load yaml file
stream = open('docker-compose-files/docker-compose3.yaml')
data = yaml.load(stream, Loader=yaml.FullLoader) # <-- deprecated


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
diagram.design()
