from flask import Flask,render_template,request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

app=Flask(__name__)

#load the model
model=pickle.load(open('parkinsonmodel.sav','rb'))

@app.route('/')
@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home')
def home():
    result=''
    return render_template('home.html',**locals())



@app.route('/predict',methods=['POST','GET'])

def predict():
    a1=float(request.form['a1'])
    a2=float(request.form['a2'])
    a3=float(request.form['a3'])
    a4=float(request.form['a4'])
    a5=float(request.form['a5'])
    a6=float(request.form['a6'])
    a7=float(request.form['a7'])
    a8=float(request.form['a8'])
    a9=float(request.form['a9'])
    a10=float(request.form['a10'])
    a11=float(request.form['a11'])
    a12=float(request.form['a12'])
    a13=float(request.form['a13'])
    a14=float(request.form['a14'])
    a15=float(request.form['a15'])
    a16=float(request.form['a16'])
    a17=float(request.form['a17'])
    a18=float(request.form['a18'])
    a19=float(request.form['a19'])
    a20=float(request.form['a20'])
    a21=float(request.form['a21'])
    a22=float(request.form['a22'])
    
    
    result=model.predict([[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22]])
    
    
    if (result[0] == 0):
        print("The Person does not have Parkinsons Disease")
        return render_template('result1.html',**locals())

    else:
        print("The Person has Parkinsons")
        return render_template('result.html',**locals())
    

if __name__ == '__main__':
    app.run(debug=True)