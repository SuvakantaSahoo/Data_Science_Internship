from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex = request.form['regex']
        matches = re.findall(regex, test_string)
        match_count = len(matches)
        return render_template('result.html', matches=matches, match_len=match_count)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
