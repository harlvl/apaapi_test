from os import getenv
from dotenv import load_dotenv

class Settings(object):
    AWS_ACCESS_KEY_ID = None
    AWS_SECRET_ACCESS_KEY = None
    AWS_ASSOCIATE_TAG = None
    
    def __init__(self):
        load_dotenv()
        try:
            self.AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
            self.AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")
            self.AWS_ASSOCIATE_TAG = getenv("AWS_ASSOCIATE_TAG")
        except:
            pass # default values
