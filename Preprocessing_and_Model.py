import re
import tensorflow as tf

from keras_preprocessing.sequence import pad_sequences
import pickle
import numpy as np
import time

def clean_Address(Address):
    Address = re.sub('[ى]', 'ي', Address)
    Address = re.sub('[إأٱآا]', 'ا', Address)
    Address = re.sub('[ؤئ]', 'ء', Address)
    Address = re.sub('[ة]', 'ه', Address)
    Address = re.sub('[%s]' % re.escape("""!"#$%&'()*+,،-./:;<=>؟?@[\]^_`{|}~"""), '', Address)  # remove punctuation
    return Address

def load_model():
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    print('loading model...')
    model= tf.keras.models.load_model('Model20Emb.h5')
    print('loading tflite model...')
    model_tflite = tf.lite.Interpreter(model_path=('Model20Emb.tflite'))
    model_tflite.allocate_tensors()
    return model,model_tflite , tokenizer



def predict(Address, model, tokenizer):
    start = time.time()
    Address = clean_Address(Address)
    max_sequence_len = model.layers[0].input_shape[1]
    token_list = tokenizer.texts_to_sequences([Address])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len, padding='pre')
    confidence = model.predict(token_list)
    exec_time = time.time() - start
    return confidence, exec_time

def predict_tflite(Address, model_tflite, tokenizer):
    start = time.time()
    Address = clean_Address(Address)
    max_sequence_len = 25
    token_list = tokenizer.texts_to_sequences([Address])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len, padding='pre')
    
    input_details = model_tflite.get_input_details()[0]

    model_tflite.set_tensor(input_details['index'], np.float32(token_list))

    model_tflite.invoke()

    output = model_tflite.get_tensor(model_tflite.get_output_details()[0]['index'])
    confidence=output.astype(np.float32)
    exec_time = time.time() - start
    return confidence, exec_time