from flask import Flask, jsonify as _j, request, render_template
import pandas as pd
import numpy as np
import pickle
import csv

heartModel = pickle.load(open("models/heart.dtc", "rb"))
spineModel = pickle.load(open("models/spine.dtc", "rb"))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.j2')

def handle_request(modelName):
        
    if modelName.lower() == 'heart':
        model = heartModel
    elif modelName.lower() == 'spine':
        model = spineModel
    else:
        return {'error': 'Model not found'}, 404

    if request.method == 'POST':
    
        output = {}
        
        app.logger.debug('Method POST')

        if request.files:
            
            for filename, file in request.files.items():

                app.logger.debug(f'Processing input file: {file.filename}')

                try:
                    try:
                        dialect = csv.Sniffer().sniff(file.stream.read(512).decode('UTF8'))
                        delimiter = dialect.delimiter
                    except:
                        delimiter = ','
                    file.stream.seek(0)
                    df = pd.read_csv(file.stream, delimiter=delimiter)
                    prediction = model.predict(df.loc[:,df.columns[0:]])
                    output.update({file.filename: prediction.tolist()})

                except Exception as e:
                    
                    msg = f"Uploaded file ('{file.filename}') is not in CSV format: {e}."
                    app.logger.error(msg)
                    output = { 'error': msg }
        
        elif request.json:

            app.logger.debug(f'JSON Input: {request.json}')

            for subject in request.json.keys():
                
                dados = request.json.get(subject)
                app.logger.debug(dados)
                df = pd.DataFrame(data=[dados])
                prediction = model.predict(df)
                output.update({subject: prediction.tolist()})
        
        else:
            
            msg = "No file nor json data has been submited"
            app.logger.error(msg)
            output = { 'error': msg }

        return _j(output)
        
    return render_template(f'{modelName.lower()}_home.j2')

@app.route('/heart', methods = ['GET', 'POST'])
def heart():
    return handle_request(modelName='heart')

@app.route('/spine', methods = ['GET', 'POST'])
def spine():
    return handle_request(modelName='spine')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
