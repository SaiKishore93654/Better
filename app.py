from flask import Flask
import bugsnag
from bugsnag.flask import handle_exceptions

app = Flask(__name__)

bugsnag.configure(
    api_key="YOUR_BUGSNAG_API_KEY",
    project_root="/app",
)

handle_exceptions(app)
@app.route("/")
def home():
    return "Hello from Flask Docker app!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
