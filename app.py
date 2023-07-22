from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('prediction.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def prediction():
    # data1 = request.form['a']
    # data2 = request.form['b']
    # data3 = request.form['c']
    # data4 = request.form['d']
    if request.method == "POST":
        features = np.array([x for x in request.form.values()])
        X = np.array(features)
    # arr = np.array([[data1, data2, data3, data4]])
    # pred = model.predict(arr)
    # return render_template('after.html', data=pred)
    return render_template('predictionhome.html')

@app.route('/prediction', methods=['POST'])
def pred_output():
    if request.method == "POST":
        features = np.array([x for x in request.form.values()])
        X = np.array(features)
    return render_template('prediction.html')

@app.route('/recommend', methods=['POST'])
def recommendation():
    # data1 = request.form['a']
    # data2 = request.form['b']
    # data3 = request.form['c']
    # data4 = request.form['d']
    # arr = np.array([[data1, data2, data3, data4]])
    # pred = model.predict(arr)
    # return render_template('after.html', data=pred)
    if request.method == "POST":
        features = np.array([x for x in request.form.values()])
        X = np.array(features)
    return render_template('recommendationhome.html')

@app.route('/recommendation', methods=['POST'])
def recommend_output():
    if request.method == "POST":
        features = np.array([x for x in request.form.values()])
        X = np.array(features)
    return render_template('recommendation.html')
    


if __name__ == "__main__":
    app.run(debug=True)