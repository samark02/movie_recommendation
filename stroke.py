import numpy as np
from flask import Flask, request, render_template,redirect,url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('stroke.pkl', 'rb'))

clf=model['model']
age=model['age']
heart_d=model['heart_disease']
bmi=model['bmi']
smoke=model['smoking_status']

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST',"GET"])
def predict():

    if request.method == "POST":
        features = np.array([float(x) for x in request.form.values()])
        print(features)
        
        # age_p = age.transform(np.array([features[0]]))
        # heart_d_p = heart_d.transform(np.array([features[1]]))
        # bmi_p =bmi.transform(np.array([features[2]]))
        # smoke_p =smoke.transform(np.array([features[3]]))

        X = np.array(features)
        y_pred=clf.predict([X])
        # print(features)
        
        if y_pred==0:
            y_pred='not likely'
        else:
            y_pred='likely'


        return render_template('index.html', prediction_text='You are {} to have a stroke'.format(y_pred))
        # return render_template('index.html', y_pred=y_pred)

    else:
        return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(debug=True)

