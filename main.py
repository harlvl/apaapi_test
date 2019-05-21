from logging import info, warning, error
from ProductAdvertisingApi import ProductAdvertisingAPI

def main():
    
    # demo_item_lookup()
    demo_item_search()


def demo_item_lookup():
    paapi = ProductAdvertisingAPI()
    item_ids = ["B007OZNUCE"]  ## sample item ids
    response = paapi.item_lookup(item_ids)
    print (response)


def demo_item_search():
    paapi = ProductAdvertisingAPI()
    parameters = {"search_index": "Kitchen", "keywords": "knife"}
    response = paapi.item_search(parameters)
    print (response)


if __name__ == "__main__":
    main()