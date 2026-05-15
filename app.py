from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Frist CI/CD Pipeline </h1><p>Welcome to the Python Web App UI.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)