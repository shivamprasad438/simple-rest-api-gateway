from flask import Flask

app = Flask(__name__)

@app.route('/')
def service2():
    return "Response from Service 2"

if __name__ == '__main__':
    app.run(port=5002)
