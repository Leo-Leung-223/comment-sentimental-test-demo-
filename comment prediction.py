import pandas as pd
import numpy as np
from google.cloud import automl_v1beta1 as automl
from google.oauth2 import service_account

# Load the csv
data =pd.read_csv('test comment.csv', encoding='utf-8')# type in your csv path

# assign project id and model id
project_id = '397901391776'
compute_region = 'us-central1'
model_id = 'TCN892922189009911808'

# Create client for prediction service.
credentials = service_account.Credentials.from_service_account_file("D:\download\gerald.json")#type in your serivce accoint key path
automl_client = automl.AutoMlClient(credentials=credentials)
prediction_client = automl.PredictionServiceClient(credentials=credentials)


# Get the full path of the model.
model_full_id = automl_client.model_path(
    project_id, compute_region, model_id
)

# Loop over the csv lines for the sentences you want to predict

# Temp dataframe to store the prediction scores
df = pd.DataFrame()

# sentence = column of interest
for row in data.values:
    snippet = str(row)
    print(snippet)
    # Set the payload by giving the content and type of the file.
    payload = {"text_snippet": {"content": snippet, "mime_type": "text/plain"}}

    # params is additional domain-specific parameters.
    # currently there is no additional parameters supported.
    params = {}
    response = prediction_client.predict(model_full_id, payload, params)

    temp = pd.DataFrame({'Negative': [response.payload[0].classification.score], #First result
                         'Positive': [response.payload[1].classification.score], #Second result
                         'Neutral': [response.payload[2].classification.score]}) # third result

    df = pd.concat([df, temp],ignore_index=True)

# Add the predicted scores to the original Dataframe
df_automl = pd.concat([data, df], axis =1)

# Export the new Dataframe,generate a csv
df_automl.to_csv("df_automl.csv", index = False,encoding="utf-8")
