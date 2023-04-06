from flask import Flask
app = Flask(__name__)


@app.route("/")
def main():
    return {"Test": "Hello test"}


if __name__ == "__main__":
    app.run()
