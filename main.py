from flask import Flask 
import pandas as pd 

df = pd.read_csv('./data/diagnoses2019.csv')

app = Flask(__name__)

@app.route('/', method=["GET"])
def home():
    return 'this is a API service for MN ICD code details'

@app.route('/', method=["GET"])
def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orients="records")
    return result

@app.route('/icd/<value>', method=["GET"])
def icdcode(value):
    print('value: ', value)
    filtered = df[df['principal_diagnosis_code']==value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orients="records")


if __name__ == '__main__':
    app.run(debug=True)
