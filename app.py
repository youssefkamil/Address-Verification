from flask import Flask, request, jsonify
import Preprocessing_and_Model as pre_model
import numpy as np

# Load the model at the begining only
global model, model_tflite, tokenizer
model, model_tflite, tokenizer = pre_model.load_model()

# __name__ represents the name of the application 
app = Flask(__name__)

@app.route('/', methods=['POST'])
def Address_verification():
    
    body = request.get_json()
    if(body['speed_up'] == True):
        confidence, exec_time = pre_model.predict_tflite(body['Address'], model_tflite, tokenizer)
    else:
        confidence, exec_time = pre_model.predict(body['Address'], model, tokenizer)

    print(body['Address'],' confidence : ', confidence[0])
    print('time : ', exec_time)
    return jsonify({'success': True ,
                    'Address': body['Address'] ,
                    'confidence': np.round(float(confidence[0][0]),4),
                    'time': exec_time})


# run the app
if __name__ == '__main__':
    app.run(debug=True)