
# from constants import QUEUES

def singleton(class_):
    instances = {}
    @staticmethod
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class locator:
    
    services = {}
    
    def get_service(self,service_name):
        return self.services[service_name]()

    def subscribe_service(self,service_name,service):
        self.services[str(service_name)] = service


