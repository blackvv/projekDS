#import model # Import the python file containing the ML model
from flask import Flask, request, render_template # Import flask libraries
import pickle

# Initialize the flask class and specify the templates directory
#app = Flask(__name__,template_folder="templates")
app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

# Default route set as 'home'
@app.route('/')
def home():
    return render_template('index.html') # Render home.html

# Route 'classify' accepts GET request
@app.route('/classify',methods=['GET'])
def classify_type():
    #try:
        k1 = request.args.get('keasyikan') 
        k2 = request.args.get('toleransi') 
        k3 = request.args.get('penarikan') 
        k4 = request.args.get('kegigihan') 
        k5 = request.args.get('pelarian') 
        k6 = request.args.get('masalah') 
        k7 = request.args.get('penipuan') 
        k8 = request.args.get('pemindahan') 
        k9 = request.args.get('konflik') 

        if k1 == "0":
            k1 = '0'
        else:
            k1 = '1'
        
        if k2 == "0":
            k2 = '0'
        else:
            k2 = '1'
        
        if k3 == "0":
            k3 = '0'
        else:
            k3 = '1'
        
        if k4 == "0":
            k4 = '0'
        else:
            k4 = '1'
        
        if k5 == "0":
            k5 = '0'
        else:
            k5 = '1'

        if k6 == "0":
            k6 = '0'
        else:
            k6 = '1'

        if k7 == "0":
            k7 = '0'
        else:
            k7 = '1'

        if k8 == "0":
            k8 = '0'
        else:
            k8 = '1'

        if k9 == "0":
            k9 = '0'
        else:
            k9 = '1'
        data = [[k1, k2, k3, k4, k5, k6, k7, k8, k9]]
        # Dictionary containing the mapping
        variety_mappings = {0: 'Normal Gamer', 1: 'Risky Gamer', 2: 'Disorder Gamer'}
        
        # Get the output from the classification model
        hasil = model.predict(data)
        variety = variety_mappings[hasil[0]]

        # Render the output in new HTML page
        return render_template('index.html', variety=variety)
    #except:
    #    return 'Error'

# Run the Flask server
if(__name__=='__main__'):
    app.run(debug=True)