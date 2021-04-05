from flask import Flask
from flask_restful import Resource, Api, reqparse
from tensorflow import keras
import numpy as np
import os

app = Flask(__name__)
api = Api(app)

model = keras.models.load_model("dnn_model")
model_features = ['Cylinders', 'Displacement', 'Horsepower', 'Weight',
                  'Acceleration', 'Model Year', 'Europe', 'Japan', 'USA']


class Predict(Resource):

    def get(self):
        return 'MPG prediction model was already loaded!', 200

    def post(self):
        # Parser to take arguments:
        parser = reqparse.RequestParser()
        for feature in model_features:
            parser.add_argument(feature, required=True, type=float)
        args = parser.parse_args()  # parse arguments to dictionary

        X = np.array(list(args.values()), ndmin=2, dtype=float)
        y = model.predict(X).squeeze().tolist()
        print('result (MPG):', y)
        return {'result (MPG)': y, 'input': str(args)}, 200


api.add_resource(Predict, '/predict')  # '/predict' is entry point for Predict


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT', 8080)))
