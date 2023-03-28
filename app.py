from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        response = requests.post('https://api.chat.com', data={'input_text': input_text})
        output_text = response.json()['output_text']
        return render_template('./index.html', output_text=output_text)
    else:
        return render_template('./index.html')

if __name__ == '__main__':
    app.run(debug=True)