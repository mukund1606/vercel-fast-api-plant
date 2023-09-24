from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
from keras.applications.vgg16 import preprocess_input
import numpy as np

ref = {0: "Healthy", 1: "Unhealthy"}


class Model:
    def __init__(self):
        self.model = load_model("models/health_detector_more_steps_best.h5")

    def isPlantHealthy(self, myImage):
        i = img_to_array(myImage)

        im = preprocess_input(i)

        img = np.expand_dims(im, axis=0)
        pred = np.argmax(self.model.predict(img))

        print(f"The prediction is {ref[pred]}")
        if ref[pred].lower() == "healthy":
            return True
        else:
            return False
