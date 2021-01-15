from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
res = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    global res
    ## Generate your recommendation here
    ## TODO

    res = {"recommendation": "recommendation1"}
    ## we are passing res as a parameter in render_template which can be accessed inside recommendation.html using jinja2 syntax.
    return render_template("recommendation.html", res=res)

@app.route('/send_recommendation_response', methods=['GET', 'POST'])
def get_recommendation_response():
    if request.form.get("accept"):
        print("store accept response in sql")
    if request.form.get("reject"):
        print("store reject response in sql")
    return home()


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8001)
