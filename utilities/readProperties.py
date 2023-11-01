import configparser
import sys
sys.path.append("/home/mohammedsalahudeen/PycharmProjects/nopcommerceApp/config.ini")
config = configparser.RawConfigParser()
config.read("/home/mohammedsalahudeen/PycharmProjects/nopcommerceApp/config.ini")
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', "baseURL")
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', "password")
        return password
