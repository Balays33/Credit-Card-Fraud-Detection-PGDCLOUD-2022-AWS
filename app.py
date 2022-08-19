from flask import Flask, request, jsonify, render_template
from datetime import datetime
import pickle

app = Flask("__name__")
# Load the model
model = pickle.load(open('model.sav', 'rb'))


@app.route("/")
def loadPage():
	return render_template('index.html')


@app.route("/", methods=['POST'])
def predict():

    # Get the first values from the HTML form
    amount = float(request.form['Amount'])
    gender = int(request.form['gender'])
    age = int(request.form['Age'])

    # Define the time-related features based on current system time
    current_time = datetime.now()

    # Determine if the current day is during the weekend or not
    day_number = current_time.weekday()
    tx_during_weekend = -1
    if day_number in (5,6):
        tx_during_weekend = 1
    else:
        tx_during_weekend = 0

    # Determine if the current time is at night (i.e. between 10pm & 6 am)
    tx_during_night = -1
    if current_time.hour <= 6 and current_time.hour >= 22:
        tx_during_night = 1
    else:
        tx_during_night = 0

    # Get the current day, month, year
    day = current_time.day
    month = current_time.month
    year = current_time.year

    # Get values for categories
    category = request.form['CATEGORY']
    CATEGORY_food_dining, CATEGORY_gas_transport, CATEGORY_grocery_net, CATEGORY_grocery_pos, CATEGORY_health_fitness, CATEGORY_home, CATEGORY_kids_pets, \
                          CATEGORY_misc_net, CATEGORY_misc_pos, CATEGORY_personal_care, CATEGORY_shopping_net, CATEGORY_shopping_pos, CATEGORY_travel = 0,0,0,0,0,0,0,0,0,0,0,0,0
    if category == 'CATEGORY_food_dining':
        CATEGORY_food_dining = 1
    elif category == 'CATEGORY_gas_transport':
        CATEGORY_gas_transport = 1
    elif category == 'CATEGORY_grocery_net':
        CATEGORY_grocery_net = 1
    elif category == 'CATEGORY_grocery_pos':
        CATEGORY_grocery_pos = 1
    elif category == 'CATEGORY_health_fitness':
        CATEGORY_health_fitness = 1
    elif category == 'CATEGORY_home':
        CATEGORY_home = 1
    elif category == 'CATEGORY_kids_pets':
        CATEGORY_kids_pets = 1
    elif category == 'CATEGORY_misc_net':
        CATEGORY_misc_net = 1
    elif category == 'CATEGORY_misc_pos':
        CATEGORY_misc_pos = 1
    elif category == 'CATEGORY_personal_care':
        CATEGORY_personal_care = 1
    elif category == 'CATEGORY_shopping_net':
        CATEGORY_shopping_net = 1
    elif category == 'CATEGORY_shopping_pos':
        CATEGORY_shopping_pos = 1
    elif category == 'CATEGORY_kids_pets':
        CATEGORY_travel = 1
                                    
    # Transform the data to pass it to the model for prediction
    data = [[amount, gender, age, tx_during_weekend, tx_during_night, day, month, year, CATEGORY_food_dining, CATEGORY_gas_transport, CATEGORY_grocery_net, \
             CATEGORY_grocery_pos, CATEGORY_health_fitness, CATEGORY_home, CATEGORY_kids_pets, CATEGORY_misc_net, CATEGORY_misc_pos, CATEGORY_personal_care, \
             CATEGORY_shopping_net, CATEGORY_shopping_pos, CATEGORY_travel]]
    output = model.predict(data)

    decision = ''
    if output[0] == 0:
        decision = 'ACCEPTED'
    else:
        decision = 'DECLINED'
    
    return render_template('index.html', prediction_text= f'Model Output: {output[0]} // Transaction {decision}')




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
