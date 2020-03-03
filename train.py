from utils import *
from model import get_model
from feature_extractor import extract_features
import pandas as pd 
dataset = pd.read_csv("./dataset/data.csv")
features = extract_features()
labels  = get_labels(dataset)

model = get_model()
model.compile(
              optimizer="rmsprop",
              loss="binary_crossentropy",
              metrics=['accuracy'])

model.fit(features, labels,
          batch_size=3,
          epochs=100)

model_json = model.to_json()
with open("./saved model/crnn.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("./saved model/crnn.h5")
print("Saved model to disk")