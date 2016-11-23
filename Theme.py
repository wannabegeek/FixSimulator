import json
import logging


class Theme(dict):
    @staticmethod
    def loadFromFile(filename):
        with open(filename) as data_file:
            data = json.load(data_file)
            return data

def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    data = Theme.loadFromFile("dark.theme")

    logging.info(data["Notebook"])
    logging.info("All done... shutting down")

if __name__ == '__main__':
    main()