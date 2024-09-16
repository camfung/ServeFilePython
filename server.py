from logging import exception
from flask import Flask, send_file


app = Flask(__name__)

AAX_FILE_PATH = ""


@app.route("/download", methods=[ "GET" ])
def download_file():
    try: 
        return send_file(AAX_FILE_PATH, as_attachment=True, mimetype="audio/aax")
    except Exception as e: 
        return str(e), 404

if __name__ == '__main__': 
    app.run(host="0.0.0.0", port=8080)
