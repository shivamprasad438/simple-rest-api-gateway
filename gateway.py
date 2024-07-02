from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Route for Service 1
@app.route('/service1/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/service1', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
def service1_proxy(path):
    url = f'http://localhost:5001/{path}'
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
    return (response.content, response.status_code, response.headers.items())

# Route for Service 2
@app.route('/service2/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/service2', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
def service2_proxy(path):
    url = f'http://localhost:5002/{path}'
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
    return (response.content, response.status_code, response.headers.items())

if __name__ == '__main__':
    app.run(port=5000)
