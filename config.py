from dotenv import load_dotenv
load_dotenv()

class Config:
    # DB Config
    # EUREKA SERVICE CONFIG
    INSTANCE_PORT = int(os.getenv('INSTANCE_PORT', 5800))
    INSTANCE_IP = os.getenv('INSTANCE_IP', '127.0.0.1')
    INSTANCE_HOST_NAME = os.getenv('INSTANCE_HOST_NAME', 'localhost')