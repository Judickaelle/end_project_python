import json
from pathlib import Path


try:
    a_file = open("stat.json", "r")
    gameRecord = json.loads(a_file.read())
    a_file.close()

    print(len(gameRecord))
    print()
    print(type(gameRecord))
    print()
    print(gameRecord)
    print()
    try:
        print(gameRecord["colors2"])
    except(KeyError):
        print("no such key for the moment")
except(FileNotFoundError):
    gameRecord = {}

key = "colors2"
value = gameRecord.get(key)      #get key value
if value == None:                     #no data available
    #create a new key
    data_list = []
    new_record = ("blue", "grey", "black")
    data_list.append(new_record)
    gameRecord[key] = data_list           #store key
    print("new key added to the dictionary")
else: 
    #update existing key
    print("key : ", value, " type : ", type(value))
#    last_record = value[-1]
#    print("last_record : ", last_record)
    new_record = ("on", "re", "tente")
    print("new_record_type : ", type(new_record))
    gameRecord[key].append(new_record)    #add new data record
    print("key updated")


a_file = open("stat.json", "w")
json.dump(gameRecord, a_file)
a_file.close()

a_file = open("stat.json", "r")
test = json.loads(a_file.read())
a_file.close()

print(len(test))
print()
print(type(test))
print()
print(test)
print()
print(test["colors2"])



#today = date.today()
#playerValue = game+"\t"+difficulty+"\t"+str(score)+"\t"+str(today)+"\n"
#my_file.write(addtofile) 
#my_file.close

#print("\nThe game has been successfully saved !")

#playerData = 

#json.dump(gameRecord, my_file)