from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
import keras
from keras.models import model_from_json
from keras.models import Model, Input
from keras.applications.vgg16 import preprocess_input,VGG16
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import LSTM,Dense,TimeDistributed,Bidirectional,Input,Conv3D,AveragePooling3D,GlobalAveragePooling2D,Flatten,GlobalAvgPool3D,GlobalAveragePooling2D,GlobalAveragePooling3D
from env_variable import *
def get_vgg_model():
#     model_feat = VGG16(weights=None, include_top=False)
    model_feat = VGG16(weights="imagenet", include_top=False)
    gap = GlobalAveragePooling2D(data_format="channels_last")(model_feat.output)
    feat_extractor=Model(inputs=model_feat.input,output=gap)
    #loading the weights from saved model
#     feat_extractor.load_weights("./saved model/model.h5")
    return feat_extractor 

def get_model(maxlen=maxlen,mode="train"):
    inputs = Input(shape=(maxlen,512))
    model = Bidirectional(LSTM(units=256, return_sequences=True))(inputs)
    # model = TimeDistributed(Dense(128,activation="relu"))(model)
    out=TimeDistributed(Dense(1,activation="sigmoid"))(model)
    model = Model(inputs, out)
    if mode=="test":
        model.load_weights("./saved model/crnn.h5")
    return model

# print(get_vgg_model().summary())
