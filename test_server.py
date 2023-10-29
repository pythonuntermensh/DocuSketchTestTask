from flask import Flask, request
import logging

app = Flask(__name__)

@app.route('/alarm', methods=['POST'])
def alarm_call():
    try:
        test_json = request.get_json()
        text = test_json["message"]
        logging.warning(text)
        return "200"
    except Exception as e:
        raise e


if __name__ == '__main__':
    app.run(debug=True)
