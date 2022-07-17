import os
import json

model_name = "model.pkl"

def train_fn(files, hyper, output):
  """ train_fn: trains the model and stores it at the given path
    - files: an array of dataset paths to fit the model with
    - hyper: hyperparameters for the model
    - output: the path where Sage Maker expects to find the model artifacts
  """

  # CREATE YOUR MODEL HERE

  # And save it
  # with open(os.path.join(output, model_name), "wb") as out:
  #   joblib.dump(model, out)
  pass

def predict_fn(model_path, features):
  """ predict_fn: given a model and a feature set, returns predictions
    - model_path: Sage Maker's standard model path
    - features: a json array of features to predict

    OUTPUT: predictions
  """

  model = None

  # with open(os.path.join(model_path, model_name), "r") as mod:
    # Retrieve your model here
    # model = joblib.load(mod)

  predictions = model.predict(features) if model == None else []

  results = {
    "results": predictions
  }

  return results
