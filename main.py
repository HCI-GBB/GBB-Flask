import json
from flask import Flask, current_app
from collections import OrderedDict

from muse import get_interest, get_focus

app = Flask(__name__)


def api_response(status, message, data):
    return current_app.response_class(
        json.dumps(OrderedDict([('status', status), ('message', message), ('data', data)]),
                   indent=None), mimetype='application/json')


@app.route('/api/v1/csv', methods=['GET'])
def post_result():
    try:
        top, interest, interest_percent = get_interest()
        focus, focus_percent = get_focus()
        return api_response(200, "취미 결과 도출 성공",
                            {"top": top, "interest": interest, "interest_percent": interest_percent, "focus": focus, "focus_percent": focus_percent}), 200
    except Exception as e:
        print("Something is wrong!!", e)
        return api_response(500, "Internal Server Error", str(e)), 500


@app.route('/')
def health_check():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
