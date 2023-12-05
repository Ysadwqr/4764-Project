from flask import Flask, request

app = Flask(__name__)
current_light_value = 0


@app.route('/light_value', methods=['POST'])
def light_value():
    global current_light_value

    light_value = int(request.args.get('light_value'))
    current_light_value = light_value

    return 'OK', 200


@app.route('/light_value', methods=['GET'])
def get_light_value():
    global current_light_value
    return str(current_light_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100)

