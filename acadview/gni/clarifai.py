import clarifai
from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='eaa76d778e2c42c9ab744314b9bf6e08')
model = app.models.get('food-items-v1.0')

response = model.predict_by_url(url='https://www.elementstark.com/woocommerce-extension-demos/wp-content/uploads/sites/2/2016/12/pizza.jpg')

print response