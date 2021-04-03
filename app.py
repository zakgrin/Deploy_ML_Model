from flask import Flask
from flask_restful import Resource, Api, reqparse
from tensorflow import keras
import numpy as np

app = Flask(__name__)
api = Api(app)

path = "dnn_model"
model = keras.models.load_model(path)  # or tf.saved_model.load(path)
model_features = ['Cylinders', 'Displacement', 'Horsepower', 'Weight',
                  'Acceleration', 'Model Year', 'Europe', 'Japan', 'USA']


class Predict(Resource):

    def get(self):
        return f'MPG prediction model ({path}) was already loaded!', 200

    def post(self):
        # Parser to take arguments:
        parser = reqparse.RequestParser()
        for feature in model_features:
            parser.add_argument(feature, required=True, type=np.float)
        args = parser.parse_args()  # parse arguments to dictionary

        X = np.array(list(args.values()), ndmin=2, dtype=np.float)
        y = model.predict(X).squeeze().tolist()
        print('result (MPG):', y)
        return {'result (MPG)': y, 'input': str(args)}, 200


api.add_resource(Predict, '/predict')  # '/predict' is entry point for Predict


if __name__ == '__main__':
    app.run()
