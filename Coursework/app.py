import os
from flask import Flask, render_template, json, url_for

app = Flask(__name__)

site_path = os.path.realpath(os.path.dirname(__file__))
json_path = os.path.join(site_path, "static/data", "pets.json")
data = json.load(open(json_path))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/pets')
def all_pets():
	return render_template('allPets.html', data=data)

@app.route('/pets/<pet>')
def single_pet(pet):
	pet_name = pet
	return render_template('pet.html', data=data , pet_name=pet_name)

@app.route('/pets/type/<petType>')
def pet_type(petType):
	pet_type = petType
	return render_template('petType.html', data=data, pet_type=pet_type)

@app.route('/pets/diet/<dietType>')
def diet_type(dietType):
	diet = dietType
	return render_template('dietType.html', data=data, diet=diet)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug = True)
