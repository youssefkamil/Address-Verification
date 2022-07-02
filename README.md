# Address-Verification
Address Verification model that takes a text of an address and verify if this address is in Cairo governorate or not with a confidence threshold

## Project Notebooks

### Data Fetching from Here API  [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)]( https://colab.research.google.com/drive/1LKY9eRcFo3i2R91m9aWSg2hNdTr6ilDe?usp=sharing )
In this Notebook I have got different addresses from different venues using random latitude and longitude inside and outside cairo 

### Data Preprocessing [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)]( https://colab.research.google.com/drive/1mDlVpjFek9t59WhXRdCZAhq2KKHSPU8x?usp=sharing )
Combining all collected data and doing some simple preprocessing to normalize the text

### Data Exploration [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)]( https://colab.research.google.com/drive/1d1bxXWRhEDOqu6-7VKY7XTQRYRO36Std?usp=sharing )
Simple Data visualization

### TensoFlow 2 Model [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)]( https://colab.research.google.com/drive/1PGZkuUoedIFF73dDn8nLIKcVtBp-EEOs?usp=sharing )
As the Problem is not complicated and the sequance is not very important, I have used simple Architecture
Also I have used different n-gram sequences of words to increase the data

### Quantize the model  [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)]( https://colab.research.google.com/drive/1LXn099IS6EiCfi8YNNIMIH8zaAKogS6A?usp=sharing )
Quantize the model with TF Lite to float32 instead of float64
This decreases the Model size from 12 MB to 1 MB and decreases the prediction time from 70 ms to 5ms

# Deployment

## Running the project
After cloning this Repo :

- To build the containers: `docker-compose build`

- To run the containers: `docker-compose up`

- The HTTP server is running on port 5000

- The POST request should be as : `{"Address":"مدينة نصر", "speed_up":0}`

- If speed_up = 0 , the prediction will be through the original model (takes around 70 ms)
- If speed_up = 1 , the prediction will be through the quantized model (takes around 5 ms)

### You can use test.py Script to test the project with some addresses

### NOTE :
#### I tried to use multiprocessing to parallelize the computetaion but it didn't work well with the LSTMs layers

## The collected dataset : 
https://drive.google.com/file/d/1-4efBWxl_yAjUQkDE0u7BTuimrUEmLiv/view?usp=sharing

https://drive.google.com/file/d/1-E93xgi9KjfaY-7-zc1TxoPdQm_0nNQ_/view?usp=sharing

https://drive.google.com/file/d/1-2s-T-iyc5ViwhuLbnivwpOwqD8ZDeqR/view?usp=sharing
