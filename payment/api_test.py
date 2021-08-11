import iyzipay
import json

options = {
    'base_url': iyzipay.base_url
}
def api_test(options):
    api_test = iyzipay.ApiTest().retrieve(options)
    temp = json.loads(api_test.read().decode('utf-8'))
    return temp['status']





