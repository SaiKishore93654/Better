from flask import Flask
import bugsnag
from bugsnag.flask import handle_exceptions
from ddtrace import patch_all, tracer

# Initialize Datadog tracing
patch_all()

# Initialize Flask
app = Flask(__name__)

# Configure Bugsnag
bugsnag.configure(
    api_key="4f52edfe22d9df72f7f4656e0ed651c4",
    project_root="."
)
handle_exceptions(app)

@app.route("/")
def hello():
    return "Hello from Flask on EKS!"

@app.route("/error")
def trigger_error():
    raise RuntimeError("Test error for Bugsnag!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
