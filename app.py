from flask import Flask
from flask import jsonify
import os #for OS program calls

app = Flask(__name__)

@app.route('/api/motion/on')
def motion_on():
    os.system("xscreensaver-command -deactivate")
    return jsonify(result='ok')

@app.route('/api/motion/off')
def motion_off():
    os.system("xscreensaver-command -activate")
    return jsonify(result='ok')

if __name__ == '__main__':
    app.run(debug=False, port=8080, host="0.0.0.0")



