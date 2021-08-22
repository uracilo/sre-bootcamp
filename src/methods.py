# These functions need to be implemented
import os

class config:
    # Database

    DATABASE_URI=['DATABASE_URI']
    DATABASE_USER=['DATABASE_USER']
    DATABASE_PASSWORD=['DATABASE_PASSWORD']
    DATABASE_NAME=["bootcamp_tht"]
    # JWT

    JWT_SECRET=['JWT_SECRET']

    # FLASK 

    FLASK_ENV=['FLASK_ENV']
    FLASK_APP=['FLASK_APP']
    FLASK_DEBUG=['FLASK_DEBUG']
    FLASK_RUN_PORT=['FLASK_RUN_PORT']


class Token:

    def generate_token(self, username, password):
        return 'test'


class Restricted:

    def access_data(self, authorization):
        return 'test'
