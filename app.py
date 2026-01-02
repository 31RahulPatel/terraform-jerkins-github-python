from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 CI/CD Successful!</h1>
    <p>Python app deployed using <b>Jenkins + Docker</b></p>
    <p>GitHub Webhook triggered this deployment automatically.</p>
    """

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
