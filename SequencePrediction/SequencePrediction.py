
from CPT import *
model = CPT()
#data,target = model.load_files("./data/train_intents.csv","./data/test_intents.csv")
data,target = model.load_files("./data/train_extracols.csv","./data/test2.csv")
model.train(data)
predictions = model.predict(data,target,3,1)
print(predictions)