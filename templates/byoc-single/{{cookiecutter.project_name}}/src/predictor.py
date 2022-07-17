
import flask
import os
import json

from algorithm.functions import predict_fn

prefix = "/opt/ml"
model_path = os.path.join(prefix, "model")

# The flask app for serving predictions
app = flask.Flask(__name__)
@app.route('/ping', methods=['GET'])
def ping():
    artifacts = os.listdir(model_path)

    status = 200 if len(artifacts) > 0 else 404

    return flask.Response(response= '\n', status=status, mimetype='application/json')


@app.route('/invocations', methods=['POST'])
def transformation():
    data = None

    if flask.request.content_type == "application/json":
        data = flask.request.json
    else:
        return flask.Response(
            response="This predictor supports JSON only", status=415, mimetype="text/plain"
        )

    predictions = predict_fn(model_path, data["features"])

    results = json.dumps({
        "predictions": predictions
    })

    return flask.Response(response=results, status=200, mimetype='application/json')
