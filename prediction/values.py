# prediction values
def predictionValues(predictions):
    predictionValues.prediction_churn_true_or_false = predictions['predictions'][0]['values'][0][0]
    predictionValues.prediction_churn_true_or_false_percentage_one = predictions['predictions'][0]['values'][0][1][0]
    predictionValues.prediction_churn_true_or_false_percentage_two = predictions['predictions'][0]['values'][0][1][1]