from flask import Flask, url_for, session, redirect, render_template, request
from authlib.integrations.flask_client import OAuth
import json
from datetime import datetime

app = Flask(__name__)
appConf = {
    "OAUTH2_CLIENT_ID": "569189205117-sja2h0ns3elm7b288tm8h9vun6fi9gms.apps.googleusercontent.com",
    "OAUTH2_CLIENT_SECRET": "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",
    "OAUTH2_META_URL": "https://accounts.google.com/.well-known/openid-configuration",
    "FLASK_SECRET": "002501c9-3417-472f-9a6c-b3db9b08c9fd",
    "FLASK FORT": 5000,
}
app.secret_key = appConf.get("FLASK_SECRET")
oauth = OAuth(app)
oauth.register(
    "myApp",
    client_id=appConf.get("OAUTH2_CLIENT_ID"),
    client_secret=appConf.get("OAUTH2_CLIENT_SECRET"),
    server_metadata_url=appConf.get("OAUTH2_META_URL"),
    client_kwargs={"scope": "openid profile email"},
)


@app.route("/")
def home():
    return render_template(
        "home.html",
        session=session.get("user"),
        pretty=json.dumps(session.get("user"), indent=4),
        datetime=(datetime.now()),
    )


@app.route("/google-login")
def googleLogin():
    return oauth.myApp.authorize_redirect(
        redirect_uri=url_for("googleCallback", _external=True)
    )


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))


@app.route("/signin-google")
def googleCallback():
    token = oauth.myApp.authorize_access_token()
    session["user"] = token
    return redirect(url_for("home"))


@app.route("/perform_logic", methods=["POST"])
def perform_logic():
    try:
        # Get the number from the request
        jsonResponse = json.loads(request.data.decode("utf-8"))

        m = [
            "F",
            "O",
            "R",
            "M",
            "U",
            "L",
            "A",
            "Q",
            "S",
            "O",
            "L",
            "U",
            "T",
            "I",
            "O",
            "N",
            "S",
            "F",
            "O",
            "R",
            "M",
            "U",
            "L",
            "A",
            "Q",
            "S",
            "O",
            "L",
            "U",
            "T",
            "I",
            "O",
            "N",
            "S",
        ]
        j = [
            "F",
            "O",
            "R",
            "M",
            "U",
            "L",
            "A",
            "Q",
            "S",
            "O",
            "L",
            "U",
            "T",
            "I",
            "O",
            "N",
            "S",
        ]

        output = []
        N = int(jsonResponse["number"])
        l = m * 7 
        k = N // 2
        
        if N > 1 and N <= 100:
            for i in range(1, k+2):
                spaces = "&nbsp;&nbsp;" * (N - (i-1) - 1)
                char = "".join(l[i-1 : ((i-1) * 3) + 1])
                output.append("<p>"+spaces + char+"</p>")
                cha = list(char)

            for i in range(k, 0, -1):
                if cha != []:
                    spaces = "&nbsp;&nbsp;" * (N - (i-1) - 1)

                    if len(cha) != 1:
                        cha.pop(0)
                        cha.pop(-1)
                    else:
                        cha.pop()

                char = "".join(cha)
                output.append("<p>"+spaces + char+"</p>")

        return output
    except Exception as err:
        return err


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
