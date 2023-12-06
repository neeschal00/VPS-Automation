import os 


def createReadme(name:str = "ServerReadme.md",title:str="README File")->bool:
    if os.path.exists(name):
        return False
    else:
        try:
            f = open(name,"w") 
            f.write("# "+title)
            f.close()
            return True
        except Exception as e:
            return False




