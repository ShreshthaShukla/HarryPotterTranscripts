 # connection to mongodb
#import Configurations
#from pymongo import MongoClient
#mongoConn = MongoClient(Configurations.HOST_NAME + ":" + str(Configurations.PORT_NAME))
#cshTransDB = mongoConn[Configurations.DATABASE_NAME]
#cshTransDB.authenticate(Configurations.DATABASE_USERNAME,
#Configurations.DATABASE_PASSWORD)

#import pymongo
import config
from pymongo import MongoClient
mongoConn = MongoClient(config.DATABASE_CONFIG['host'] + ":" + str(config.DATABASE_CONFIG['port']))
database = mongoConn[config.DATABASE_CONFIG['dbname']]
database.authenticate(config.DATABASE_CONFIG['user'],
config.DATABASE_CONFIG['password'])