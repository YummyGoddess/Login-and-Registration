from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)

@app.reoute("/")
def index():
    return render_template("index.html")

@app.route.("/reserve", methods=['POST'])
def reserve():
    debugHelp("RESERVE METHOD")
    return "reserve"
@app.route("/success")
def success():
    return "Thank you ____. Your seat is now reserved!"
def debugHelp(message = ""):
        print("\n\n-------------------------", message, "---------------")
        print('REQUEST.FORM' request.from)
        print('SESSION:', session)
        if __name__ == "__main__":
        app.run(debug=True)
