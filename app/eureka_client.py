import py_eureka_client.eureka_client as eureka_client
from config import Config

def define_eureka_client():
    eureka_client.init(
        eureka_server=Config.EUREKA_SERVER,
        app_name=Config.APP_NAME,
        instance_port=Config.INSTANCE_PORT,
        instance_host= Config.INSTANCE_HOST_NAME
    )
