import bottlenose

from logging import info, warning, error
from ProductAdvertisingApi import ProductAdvertisingAPI

def main():
    ## create instance
    paapi = ProductAdvertisingAPI()
    item_ids = ["B007OZNUCE"]  ## sample item ids

    ## get response
    response = paapi.item_lookup(item_ids)

    ##display raw bs4 response
    print (response)


if __name__ == "__main__":
    main()