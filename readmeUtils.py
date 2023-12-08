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


def writeBody(content:str)->str:

    with open("ServerReadme.md", "r") as filew:
        existing_content = filew.read()

    title, *body_lines = existing_content.split("##", 1)
    body_content = "\n".join(body_lines).strip()

    updated_content = f"{title}##{body_content}\n{content}"

    with open("ServerReadme.md", "w") as updateW:
        updateW.write(updated_content)
    



