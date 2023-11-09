from flask import Flask,url_for,session,redirect,render_template
from authlib.integrations.flask_client import OAuth
import json
from datetime import datetime
app=Flask(__name__)
appConf={
"OAUTH2_CLIENT_ID": "569189205117-sja2h0ns3elm7b288tm8h9vun6fi9gms.apps.googleusercontent.com",

"OAUTH2_CLIENT_SECRET": "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",
 "OAUTH2_META_URL": "https://accounts.google.com/.well-known/openid-configuration", 
 "FLASK_SECRET": "002501c9-3417-472f-9a6c-b3db9b08c9fd",

"FLASK FORT": 5000
}
app.secret_key=appConf.get("FLASK_SECRET")
oauth=OAuth(app)
oauth.register("myApp",
               client_id=appConf.get("OAUTH2_CLIENT_ID"),
               client_secret=appConf.get("OAUTH2_CLIENT_SECRET"),
               server_metadata_url=appConf.get("OAUTH2_META_URL"),
               client_kwargs={
                   "scope":"openid profile email"}
)
@app.route("/")
def home():
    return render_template("home.html",session=session.get("user"),pretty=json.dumps(session.get("user"),indent=4),datetime = (datetime.now()))

@app.route("/google-login")
def googleLogin():
    return oauth.myApp.authorize_redirect(redirect_uri=url_for("googleCallback",_external=True))

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("home"))
@app.route("/signin-google")
def googleCallback():
    token=oauth.myApp.authorize_access_token()
    session["user"]=token
    return redirect(url_for("home"))
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)