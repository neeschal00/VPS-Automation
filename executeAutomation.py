import os
import json 
from typing import Union

def readJson(file:str="vps.json")-> Union[list,None]:
    try:
        with open(file,"r") as jsonF:
            data = jsonF.read()
        
        return json.loads(data)
    except Exception as e:
        print(e)
        return None






