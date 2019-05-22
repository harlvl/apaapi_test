import bottlenose
from bs4 import BeautifulSoup
from app_settings import Settings
from logging import info, warning, error

class ProductAdvertisingAPI(object):
    env = Settings()
    amazon = None
    is_valid = False  ##for now it means the provided credentials are valid

    def __init__(self):
        try:
            self.amazon = bottlenose.Amazon(
                AWSAccessKeyId = self.env.AWS_ACCESS_KEY_ID,
                AWSSecretAccessKey = self.env.AWS_SECRET_ACCESS_KEY,
                AssociateTag = self.env.AWS_ASSOCIATE_TAG,
                Parser = lambda response_text: BeautifulSoup(response_text, 'lxml'))
            self.is_valid = True
        except Exception as e:
            print(e)
            print("Invalid credentials for amazon object")
            self.amazon = None
            self.is_valid = False

    def is_valid(self):
        return self.is_valid
    
    def item_lookup(self, item_ids):
        """
        :param item_ids: the item ids
        :type item_ids: list
        :return: parsed xml
        :rtype: bs4.BeautifulSoup
        """
        if not self.amazon or not self.is_valid:
            print("Amazon object is not valid")
            return None
        try:
            return self.amazon.ItemLookup(ItemId=','.join(item_ids))
        except Exception as e:
            print(e)
            print("Amazon object invalid, check credentials")
            return None

    def item_search(self, parameters):
        ##TODO documentation
        search_index = parameters['search_index']
        keywords = parameters['keywords']
        try:
            return self.amazon.ItemSearch(SearchIndex=search_index, Keywords=keywords)
        except Exception as e:
            print(e)
            print("Probably credentials")
            return None

