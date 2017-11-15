from clarifai.rest.client import ClarifaiApp

app = ClarifaiApp(api_key='ef0f24a2dc7f413c9d781911db82261b')

model = app.models.get('fa07ebd275514870a636b345aa3e1434')

print(model.predict_by_filename('taylor.png'))

