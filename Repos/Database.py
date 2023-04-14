'''
Created on 02-Feb-2023
@author: Dell
'''
from mongoengine import *
import urllib
uri="mongodb+srv://mongo_shubhajoy:mongo_shubhajoy@cluster0.tuetzli.mongodb.net/?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE&w=majority"
connect(host=uri)
class User(Document):
    name = StringField()
#nirmoyb@gmail.com    