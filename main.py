import requests
import json
from django.core.serializers import serialize

def getJson( theapicat ):
    try:
        response = requests.get(theapicat)
        convertjson = response.json()
        
        responsejson = json.dumps(convertjson, indent=6)
        cats = json.loads(responsejson)
        
        for i in cats:
            #if i["origin"] in cats:
            print("origin: " + i['origin']) 
            print("temperament: " + i["temperament"])
            print("Description: " + i["description"])
        
    except Exception as err:
        print(f'Error occurred: {err}')

    return cats    

def getBreed( cats ):
    cats_breeds = getJson( cats )
    try:
        for breeds in cats_breeds:
            #print("cfa_url" + i["cfa_url"])
            #for url in breeds:
                #while count <= 3:
            if "cfa_url" in breeds:
                print(breeds["cfa_url"])
    
    except Exception as err:
        print(f'cfa_url does not exist for this breed: {err}')   
        
           
if __name__ == '__main__':
    #getJson("https://api.thecatapi.com/v1/breeds")
    getBreed("https://api.thecatapi.com/v1/breeds")


############################### NOTES ###############################################
#The json library has two main functions:                                           #
#                                                                                   #
#json.dumps() — Takes in a Python object, and converts (dumps) it to a string.      #
#json.loads() — Takes a JSON string, and converts (loads) it to a Python object.    #
# # print output as json format                                                     #
#responsejson = json.dumps(convertjson, indent=6)                                   #                      
############################### NOTES ###############################################        



