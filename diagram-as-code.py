from diagrams import Cluster, Diagram as DaC, Edge
from service import Service
from diagrams.k8s.storage import Volume
from diagrams.onprem.compute import Server

#onPrem imports
from diagrams.onprem.database import Mysql as MySQL
from diagrams.onprem.database import Postgresql as PostgreSQL
from diagrams.onprem.network import Zookeeper
from diagrams.onprem.queue import Kafka

cluster_attr = {
    "bgcolor": "transparent",
    "pencolor" : "white",
}

with DaC("mysql postgres dblog zookeeper kafka ", filename= "./diagram-adhocBT", show=True, direction="BT"):
    with Cluster(" ", graph_attr=cluster_attr):
        with Cluster("mysql service"):
            mysql = MySQL("mysql")

        with Cluster("postgres service"):
            postgres = PostgreSQL("postgres")
        vol_mysql = Volume("db-data")
        vol_mysql >> Edge(color="darkgreen", style="dashed") << mysql

        vol_postgres = Volume("db-data")
        vol_postgres >> Edge(color="darkgreen", style="dashed") << postgres

    with Cluster("dblog service"):
        dblog = Server("dblog")

    with Cluster("  ", graph_attr=cluster_attr):
        with Cluster("zookeeper service"):
            zookeeper = Zookeeper("zookeeper")

        with Cluster("kafka service"):
            kafka = Kafka("kafka")

    vol_kafka = Volume("/var/run/docker.sock")
    vol_kafka >> Edge(color="darkgreen", style="dashed") << kafka
    kafka >> zookeeper
    dblog - zookeeper
    dblog >> mysql
    dblog >> postgres
    kafka - zookeeper


    # dblog >> mysql
    # dblog >> postgres
    # kafka >> zookeeper
    # dblog - zookeeper
    # kafka - zookeeper
