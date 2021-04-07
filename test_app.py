import requests
import unittest
import ast
import argparse


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
                      'Weight': 3850.0, 
                      'Acceleration': 8.5,
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
    url_endpoint = '/predict'
    host_option = 'cloud'
    if host_option == 'local':
        url = 'http://127.0.0.1:8080' + url_endpoint
    if host_option == 'cloud':
        url = 'https://auto-mpg-predict-jdywf5v6pa-uc.a.run.app' + url_endpoint
    unittest.main()

    # Todo:
    # parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    # parser.add_argument('-ep', '--endpoint', default='/predict', metavar='',
    #                     help="API endpoint (default: /predict)")
    # subparser = parser.add_subparsers(help='selection', dest='host_option')
    # # local:
    # local_parser = subparser.add_parser('local', aliases=['l'],
    #                                     help='local api option (machine or docker)',
    #                                     formatter_class=argparse.RawTextHelpFormatter)
    # local_parser.add_argument('-p', '--port', default='8080', type=str,
    #                           help="Local API port (default: 8080)")
    # local_parser.add_argument('-host', '--host', default='http://127.0.0.1', type=str, metavar='',
    #                           help="Local API host (default: http://127.0.0.1)")
    # # cloud:
    # cloud_parser = subparser.add_parser('cloud', aliases=['c'],
    #                                     help='cloud api option (GCP)',
    #                                     formatter_class=argparse.RawTextHelpFormatter)
    # cloud_parser.add_argument('-host', '--host',
    #                           default='https://auto-mpg-predict-jdywf5v6pa-uc.a.run.app',
    #                           type=str, metavar='',
    #                           help="Cloud API host (default: https://auto-mpg-predict-jdywf5v6pa-uc.a.run.app)")
    # args = parser.parse_args()
    # print(args)
    # url_endpoint = '/predict'
    # if args.host_option == 'local':
    #     url = 'http://127.0.0.1:8080' + url_endpoint
    # if args.host_option == 'cloud':
    #     url = 'https://auto-mpg-predict-jdywf5v6pa-uc.a.run.app' + url_endpoint
    #
    # print('URL:', url, '(make sure that app.py is running in this host)')
