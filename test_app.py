import requests
import unittest
import ast


url_option = 'local'
if url_option == 'local':
    url = 'http://127.0.0.1:5000/predict'
elif url_option == 'docker':
    url = 'http://0.0.0.0:8080/predict'
elif url_option == 'gcp':
    url = 'https://predict-mpg-jdywf5v6pa-uc.a.run.app/predict'
print('URL option: {0} (make sure that app.py is running in {0})'.format(url_option))
print('Selected URL:', url)


class TestApp(unittest.TestCase):

    def test_get(self):
        get_request = requests.get(url)
        self.assertTrue(get_request.ok)
        self.assertEqual(get_request.status_code, 200)
        self.assertEqual(get_request.text, '"MPG prediction model was already loaded!"\n')

    def test_post(self):
        input_data = {'Cylinders': 8.0,
                      'Displacement': 390.0,
                      'Horsepower': 190.0,
                      'Weight': 3850.0, 'Acceleration': 8.5,
                      'Model Year': 70.0,
                      'Europe': 0.0,
                      'Japan': 0.0,
                      'USA': 1.0}

        post_request = requests.post(url, data=input_data)
        post_result = post_request.json()
        post_result['input'] = ast.literal_eval(post_result['input'])

        self.assertTrue(post_request.ok)
        self.assertEqual(post_request.status_code, 200)
        self.assertEqual(input_data, post_result['input'])
        self.assertEqual(post_result['result (MPG)'], 15.818567276000977)


if __name__ == '__main__':
    unittest.main()