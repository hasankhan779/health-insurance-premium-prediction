from flask import Flask ,render_template, request
import pickle
app = Flask(__name__)
@app.route('/')
def fun1():
    return render_template('HealthINS.html')
@app.route('/predict',methods =['POST'])
def fun2():
    name = request.form['Name']
    age = int(request.form['Age'])
    bmi = float(request.form['BMI'])
    smoker = 1 if request.form['Smoker'] == 'Y' else 0
    mymodel = pickle.load(open('model2.pkl','rb'))
    premium = round(mymodel.predict([[age,bmi,smoker]])[0],2)
    return '<h1>Hi {},Your predicted premium is {} </h1>'.format(name,premium)
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host = '0.0.0.0',port =8080)