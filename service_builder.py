from service import Service

class ServiceBuilder():
    def __init__(self, name, dict):
        self.__name = name
        self.__dict = dict
        self.__image_name = None
        self.__container_name = None
        self.__volumes = []  #List of volumes
        self.__depends_on = [] #Service depends on other services

    def with_image_name(self):
        dict = self.__dict
        if(dict.get('image') is not None):
            self.__image_name = dict.get('image')
        elif(dict.get('build') is not None):
            build = dict.get('build')
            if(build.get('container_name') is not None):
                self.__image_name = build.get('container_name')
            else:
                self.__image_name = build
        return self

    def with_container_name(self):
        dict = self.__dict
        if(dict.get('container_name') is not None):
            self.__container_name = dict.get('container_name')
        elif(dict.get('build') is not None):
            build = dict.get('build')
            if(build.get('container_name') is not None):
                self.__container_name = build.get('container_name')
        return self

    # Todo: is not finished
    def with_volumes(self):
        data_volumes = self.__dict.get('volumes')
        if(data_volumes is not None):
            for v in data_volumes:
                if(type(v) is str):
                    volume = v.split(":")[0]
                else:
                    volume = v.get('source')
                self.__volumes.append(volume)
        return self

    # Todo: is not finished
    def with_depends_on(self):
        data_depends_on = self.__dict.get('depends_on')
        if(data_depends_on is not None):
            for don in data_depends_on:
                self.__depends_on.append(don)
        return self

    def build(self):
        # ... make something
        return Service(
            self.__name,
            self.__image_name,
            self.__container_name,
            self.__volumes,
            self.__depends_on)
