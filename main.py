from flask import Flask, render_template


app = Flask(__name__)
app.config.from_pyfile('settings/development_settings.cfg')


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()