from flask import Flask,render_template,request
import numpy as np
import pickle

app = Flask(__name__)
sc = pickle.load(open('sc.pkl', 'rb'))
model = pickle.load(open('classifier.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    pred = model.predict( sc.transform(final_features) )
    return render_template('pred.html', prediction = pred)
 
# main driver function
if __name__ == '__main__':
  app.run(debug = True)