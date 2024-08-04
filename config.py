from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    # DB Config
    # EUREKA SERVICE CONFIG
    EUREKA_SERVER = os.getenv('SERVICE_URL', 'http://admin:PasswordEurekaServer@localhost:8761/eureka')  # if you are using eureka service discovery
    APP_NAME = os.getenv('APP_NAME', 'stamping-document-service') # if you are using eureka service discovery
    INSTANCE_PORT = int(os.getenv('INSTANCE_PORT', 5800)) 
    INSTANCE_HOST_NAME = os.getenv('INSTANCE_HOST_NAME', 'localhost') 
    WKHTMLTOPDF = os.getenv('WKHTMLTOPDF','C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe') # path to wkhtmltopdf