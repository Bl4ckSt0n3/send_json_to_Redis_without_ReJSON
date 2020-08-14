import redis
import random
import ast

random.seed(444)

with open("new.json","r") as file:


    content = file.read()

    dictionaryFile = ast.literal_eval(content)

    data = {"id:{}".format(random.getrandbits(32)): i for i in dictionaryFile}


redisDB = redis.Redis(db=1)


with redisDB.pipeline() as pipe:
    
    for id0, id1 in data.items():
        
        pipe.hmset(id0, id1)
    
    pipe.execute()

redisDB.bgsave()





    
    









"""
print(data.items())
print(type(data))

data = {"id:{}".format(random.getrandbits(32)): i for i in (file)}

redisDB = redis.Redis(db=1)


with redisDB.pipeline() as pipe:
    for id0, id1 in data.items():
        pipe.hmset(id0, id1)
    pipe.execute()

redisDB.bgsave()


"""


