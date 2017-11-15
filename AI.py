from clarifai.rest import ClarifaiApp

app = ClarifaiApp()

model = app.models.get('fa07ebd275514870a636b345aa3e1434')

print(model.predict_by_filename('taylor.png'))

