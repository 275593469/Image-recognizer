from flask import Flask, request
import json

import main

app = Flask(__name__)

@app.route('/event-invoke', methods = ['POST', 'GET'])
def invoke():
    # Get all the HTTP headers from the official documentation of Tencent
    request_id = request.headers.get("X-Scf-Request-Id", "")
    print("SCF Invoke RequestId: " + request_id)

    # event = request.get_data()
    # event_str = event.decode("utf-8")
    # if event_str:
    #     # event_str转成字典
    #     json_data = json.loads(event_str)
    #     print("event", json_data)
    #     bucket = json_data.get('bucket')
    #     fileName = json_data.get('fileName')
    # #     todo
    image_path = './1711206604151.png'
    res = main.selector_image(image_path)
    result = '分类：' + res
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)

