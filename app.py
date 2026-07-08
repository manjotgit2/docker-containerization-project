from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Flask App</title>
        <style>
            body{
                background:#f4f6f9;
                font-family:Arial,sans-serif;
                text-align:center;
                padding-top:100px;
            }

            .card{
                width:600px;
                margin:auto;
                background:white;
                padding:40px;
                border-radius:15px;
                box-shadow:0px 0px 15px gray;
            }

            h1{
                color:#2E86C1;
            }

            p{
                font-size:20px;
            }

            .success{
                color:green;
                font-weight:bold;
            }
        </style>
    </head>

    <body>

        <div class="card">

            <h1>🐳 Docker Flask Application</h1>

            <p>Welcome to my DevOps Project</p>

            <p class="success">
            ✔ Application is running successfully inside Docker Container
            </p>

            <hr>

            <h3>Created By</h3>

            <p>Manjot Kaur</p>

            <p>MCA | DevOps Internship Project</p>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
