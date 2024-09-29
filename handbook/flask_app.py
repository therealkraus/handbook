# Standard Libary Imports
from pathlib import Path

# Related third party imports
from flask import Flask, send_from_directory

# Local application/library specific imports

app = Flask(__name__, static_folder="site")


@app.route("/", defaults={"url_path": ""})
@app.route("/<path:url_path>")
def serve(url_path: str):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        raise ValueError(
            """No static folder found for the Flask app.
               You can set the static folder by specifying the `static_folder` parameter in the `Flask` constructor.
               e.g. `app = Flask(__name__, static_folder="site")`"""
        )

    normalized_path = Path(static_folder_path) / url_path
    if Path.is_dir(normalized_path):
        if Path.exists(normalized_path / "index.html"):
            return send_from_directory(normalized_path, "index.html")

    if Path.exists(normalized_path):
        return send_from_directory(static_folder_path, url_path)

    return send_from_directory(static_folder_path, "404.html"), 404
