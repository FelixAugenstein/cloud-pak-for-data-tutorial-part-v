from flask import Flask, request, render_template, json, url_for
from decouple import config

app = Flask(__name__, template_folder='template')

# Local env variables
API_KEY = config('apikey')
URL = config('url')
SPACE_ID = config('space_id')
DEPLOYMENT_ID = config('deployment_id')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    state = request.form['state']
    account_length = request.form['account_length']
    area_code = request.form['area_code']
    international_plan = request.form['international_plan']
    voice_mail_plan = request.form['voice_mail_plan']
    number_vmail_messages = request.form['number_vmail_messages']
    total_day_minutes = request.form['total_day_minutes']
    total_day_calls = request.form['total_day_calls']
    total_day_charge = request.form['total_day_charge']
    total_eve_minutes = request.form['total_eve_minutes']
    total_eve_calls = request.form['total_eve_calls']
    total_eve_charge = request.form['total_eve_charge']
    total_night_minutes = request.form['total_night_minutes']
    total_night_calls = request.form['total_night_calls']
    total_night_charge = request.form['total_night_charge']
    total_intl_minutes = request.form['total_intl_minutes']
    total_intl_calls = request.form['total_intl_calls']
    total_intl_charge = request.form['total_intl_charge']
    customer_service_calls = request.form['customer_service_calls']

    # wml authentication
    from ibm_watson_machine_learning import APIClient

    wml_credentials = {
                    "url": URL, # the default url for wml services in the US is https://us-south.ml.cloud.ibm.com
                    "apikey": API_KEY
                    }

    client = APIClient(wml_credentials)
    print(client.version)

    # deployment space
    space_id = SPACE_ID
    client.set.default_space(space_id)

    # deployment id
    deployment_id = DEPLOYMENT_ID

    # test deployment with test data
    scoring_data = {
        client.deployments.ScoringMetaNames.INPUT_DATA: [
            {
                "fields": ["state", "account length", "area code", "international plan", "voice mail plan", "number vmail messages", "total day minutes", "total day calls", "total day charge", "total eve minutes", "total eve calls", "total eve charge", "total night minutes", "total night calls", "total night charge", "total intl minutes", "total intl calls", "total intl charge", "customer service calls"], 
                "values": [[state,account_length,area_code,international_plan,voice_mail_plan,number_vmail_messages,total_day_minutes,total_day_calls,total_day_charge,total_eve_minutes,total_eve_calls,total_eve_charge,total_night_minutes,total_night_calls,total_night_charge,total_intl_minutes,total_intl_calls,total_intl_charge,customer_service_calls]]
            }]
    }
    print(scoring_data)

    predictions = client.deployments.score(deployment_id, scoring_data)
    print("The Prediction output regarding customer churn will be displayed in this format 1 for True or 0 for False: \n ", predictions)

    # import values.py
    from prediction import values
    values.predictionValues(predictions)

    # obtain variables from values.py
    prediction_churn_true_or_false = values.predictionValues.prediction_churn_true_or_false
    prediction_churn_true_or_false_percentage_one = values.predictionValues.prediction_churn_true_or_false_percentage_one
    prediction_churn_true_or_false_percentage_two = values.predictionValues.prediction_churn_true_or_false_percentage_two

    # import rules.py
    from prediction import rules
    rules.predictionRules(prediction_churn_true_or_false, prediction_churn_true_or_false_percentage_one, prediction_churn_true_or_false_percentage_two)
    
    # obtain variables from rules.py
    churn_result = rules.predictionRules.churn_result
    print(churn_result)
    churn_result_percentage = rules.predictionRules.churn_result_percentage
    print(churn_result_percentage)

    return render_template('result.html', state=state, account_length=account_length, area_code=area_code, international_plan=international_plan, voice_mail_plan=voice_mail_plan, number_vmail_messages=number_vmail_messages, total_day_minutes=total_day_minutes, total_day_calls=total_day_calls, total_day_charge=total_day_charge, total_eve_minutes=total_eve_minutes, total_eve_calls=total_eve_calls, total_eve_charge=total_eve_charge, total_night_minutes=total_night_minutes, total_night_calls=total_night_calls, total_night_charge=total_night_charge, total_intl_minutes=total_intl_minutes, total_intl_calls=total_intl_calls, total_intl_charge=total_intl_charge, customer_service_calls=customer_service_calls, predictions=predictions, churn_result=churn_result, churn_result_percentage=churn_result_percentage)


if __name__ == '__main__':
    app.run(debug=True)