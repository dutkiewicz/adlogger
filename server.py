import os
import json
from flask import Flask, request, Response

app = Flask(__name__)
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__name__)), 'logfile.log')


@app.route('/', methods = ['GET'])
def main():
    if request.method == 'GET':
        with open(LOG_FILE, 'a') as file:
            file.write(json.dumps(request.args) + '\n')
        return Response(status=200)
    else:
        return Response(status=404)

if __name == '__main__':
    app.run()