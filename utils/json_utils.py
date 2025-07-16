from uuid import uuid4
import json

ID_KEY = "id"
PARENT_ID_KEY = "parentId"

def str_to_json(str_content):
    json_contnet = extract_between_braces(json_contnet)
    json_contnet = json_contnet.replace('\n',' ')
    json_contnet = json.loads(json_contnet)
    return json_contnet

def id_json(parent_id, json_contnet):
    json_contnet[ID_KEY] = str(uuid4())
    json_contnet[PARENT_ID_KEY] = parent_id
    
    for module in json_contnet["children"]:
        module[ID_KEY] = str(uuid4())
        module[PARENT_ID_KEY] = json_contnet[ID_KEY]
        
        for lesson in module["children"]:
            lesson[ID_KEY] = str(uuid4())
            lesson[PARENT_ID_KEY] = module[ID_KEY]
            
            for topic in lesson["children"]:
                topic[ID_KEY] = str(uuid4())
                topic[PARENT_ID_KEY] = lesson[ID_KEY]
                
    return json_contnet

def extract_between_braces(input_string):
    start_index = input_string.find('{')
    end_index = input_string.rfind('}')
    
    if start_index != -1 and end_index != -1 and start_index < end_index:
        return input_string[start_index:end_index+1]
    else:
        return None