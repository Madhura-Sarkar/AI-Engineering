class AIModel:
    def __init__(self, model_name):
        self.model_name = model_name        
    def predict(self):
        print("predicting...")
    
class TextModel(AIModel):
    def __init__(self, model_name):
        super().__init__(model_name)
    def predict(self):
        print(f"{self.model_name} is predicting text...")
    

class ImageModel(AIModel):
    def __init__(self, model_name):
        super().__init__(model_name)
    def predict(self):
        print(f"{self.model_name} is predicting image...")
        
aimodel = AIModel("base_model")
text_model = TextModel("text model")
image_model = ImageModel("image model")

text_model.predict()
image_model.predict()
        