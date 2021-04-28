import os
import re
from flask import Flask,jsonify

data_file = 'textfile.txt'
app = Flask(__name__)
@app.route("/search")
def search():
    search_lines = []
    q = "Cheese"
    with open(data_file,"r") as f:
        for number,line in enumerate(f.readlines()):
            x = re.search(q, line)
            if x:
                number +=1
                numLine = str(number) +' ,'+line
                search_lines.append(numLine)
    with open('SKU.txt', 'w') as f:
        for item in search_lines:
            f.write("%s" % item)

    return jsonify(search_lines)

if __name__ == '__main__':
    HTTP_PORT = 8080
    port = int(os.getenv('VCAP_APP_PORT', HTTP_PORT))
    app.run(host='localhost', port=port, threaded=True)

