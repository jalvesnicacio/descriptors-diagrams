from diagrams import Cluster, Diagram, Edge
from service import Service

import yaml

#load yaml file
stream = open('docker-compose.yaml')
data = yaml.load(stream)

#start diagram diagram_name
diagram_name = ""

services = data['services']


#Create name of diagram:
for key in services:
    diagram_name = diagram_name + key + " "

#start diagram:
with Diagram(diagram_name, filename="./diagram", show=False) as target:
    #each service as a diagram cluster:
    for key in services:
        dict_service = services[key]
        #print(key + " ::=> \n")
        #print(dict_service)
        srv = Service(key, dict_service)
        srv.design()
