# prediction rules for customer churn true or false
def predictionRules(prediction_churn_true_or_false, prediction_churn_true_or_false_percentage_one, prediction_churn_true_or_false_percentage_two):
    if prediction_churn_true_or_false == 0 or prediction_churn_true_or_false == "no" or prediction_churn_true_or_false == "False":
        predictionRules.churn_result = "This customer will not churn."
    elif prediction_churn_true_or_false == 1 or prediction_churn_true_or_false == "yes" or prediction_churn_true_or_false == "True":
        predictionRules.churn_result = "This customer will churn."
    else:
        predictionRules.churn_result = "There is no accurate prediction for this customer." 

    # prediction rules for confidence score
    if prediction_churn_true_or_false_percentage_one > prediction_churn_true_or_false_percentage_two:
        predictionRules.churn_result_percentage = "The confidence score is: " +str(prediction_churn_true_or_false_percentage_one * 100)+"%"
    elif prediction_churn_true_or_false_percentage_one < prediction_churn_true_or_false_percentage_two:
        predictionRules.churn_result_percentage = "The confidence score is: " +str(prediction_churn_true_or_false_percentage_two * 100)+"%"
    else:
        predictionRules.churn_result_percentage = "There is no accurate confidence score for this prediction."    
