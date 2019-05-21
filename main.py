import bottlenose
import os

from dotenv import load_dotenv
from logging import info, warning, error

def main():
    load_dotenv()
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_ASSOCIATE_TAG = os.getenv("AWS_ASSOCIATE_TAG")

    amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG)
    response = amazon.ItemLookup(ItemId="B007OZNUCE")
    print(response)


if __name__ == "__main__":
    main()