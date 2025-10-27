import os
import subprocess
import shlex
import flask

app = flask.Flask(__name__)


@app.route("/route_param/<route_param>")
def route_param(route_param):

    # Fixed: Use subprocess with list of arguments to prevent command injection
    # Never pass user input directly to shell commands
    try:
        result = subprocess.run(
            [route_param],  # Pass as list, not through shell
            capture_output=True,
            text=True,
            timeout=5,
            check=False
        )
        return f"Output: {result.stdout}"
    except Exception as e:
        return f"Error: {str(e)}", 400


# Flask true negatives
@app.route("/route_param/<route_param>")
def route_param2(route_param):

    # ok:dangerous-os-exec
    os.execl("static")

    return "ok!"
