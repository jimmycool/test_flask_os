'''
Created on 21-Feb-2023

@author: Dell
'''
from django.shortcuts import render
from django.http import HttpResponse
from Repos  import Database 
import mongoengine
from pymongo import MongoClient
from django.http.response import JsonResponse
import pymongo
uri="mongodb+srv://mongo_shubhajoy:mongo_shubhajoy@cluster0.tuetzli.mongodb.net/?retryWrites=true&w=majority$&ssl=true&ssl_cert_reqs=CERT_NONE"
def index(request):
    return render(request, "index.html")
def connect1(request):
    global uri
    client = MongoClient(uri,connect=False).list_database_names()
    collections=MongoClient(uri).get_database('sample_airbnb').list_collection_names()
    v=MongoClient(uri,connect=False).get_database('sample_airbnb')
    databases={"databases":client,"collections":collections}
    databases={"databases":client,"collections":collections}
    return JsonResponse(databases,safe=False)
def connect2(request):
    global uri
    u=Database.User(name="Sdas")
    u.save()
    return render(request, "index.html")
