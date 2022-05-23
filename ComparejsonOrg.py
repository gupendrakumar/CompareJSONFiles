import os, json

def compare_dict(a,b):    
    if len(a) != len(b):
        print("\n print len of prod data from compare_dict: \n", len(a))   
        print("\n print len of QA data from compare_dict: \n", len(b))   
        return False    
    else:       
        for x,y in a.items():          
            if not x in b:             
                return False
                print('difference in the object is', x)
            else:             
                if not compare_object(y, b[x]):                
                    return False    
                    print('difference in the object is', y)
    return True
 
def compare_list(a,b):    
    if len(a) != len(b):       
        return False    
    else:       
        for i in range(len(a)):          
            if not compare_object(a[i], b[i]):             
                return False    
    return True 
    print('difference in the object is', a)


def compare_object(a,b):
    if type(a) != type (b):
        print('\n difference in type of the object: \n', a ,'\n and \n second file: \n', b)
        return False
    elif type(a) is dict:
        print("\n confirming it is dict type \n And \n calling def compare_dict with data as below:\n prod data:", a ,"\n and \n QA data: \n", b)
        return compare_dict(a,b)
    elif type(a) is list:
        print("\n confirming it is list \n prod data: \n", a ,"\n and QA data: \n", b)
        return compare_list(a,b)
    else:
        return a == b

path_to_json = './' #Make sure to keep the json files in the same direcotry as that of this .py script.
json_files = [oh_json for oh_json in os.listdir(path_to_json) if oh_json.endswith('.json')]

#below for loop is to seggregate Prod and other json.
# Please keep 'PROD' in file name of production json file.
# Please keep 'QA' in file name of QA json file.
for i in range(0, len(json_files)):
   if 'PROD' in json_files[i]:
        Prodjson = json_files[i]
        print('PROD file is', Prodjson)
   elif 'QA' in json_files[i]:
         Qajson = json_files[i]
         print('QA file is', Qajson)

## Open Production json and load.
with open(Prodjson) as f:
    proddata = json.load(f)

## validate json of prod
#isValid = validateJSON(Prodjson)
#print("Given JSON string is Valid", Prodjson , isValid)

## Open QA json and load.
with open(Qajson) as g:
   qadata = json.load(g)

## valiadte QA json.
#isValid = validateJSON(Qajson)
#print("Given JSON string is Valid", isValid)

# Compare Objects/Dict/List of files passed onto.
print(compare_object(proddata, qadata))
