from flask import Flask, jsonify, abort, request
from views import dict_data_base
from flasgger import Swagger

app = Flask(__name__)


@app.route("/deposits", methods=["GET"]) #GET вернуть данные после обработки
def get_deposit():
    # language=YAML
    """
    Get deposit info
    ---
    tags:
        - Deposit
    parameters:
          - in: path
            name: parametrs
            type: string
            required: true
            schema:
                $ref: "#/definitions/Deposit"
    responses:
        200:
            description: Deposit
            schema:
                id: Deposit
                properties:
                    data:
                        type: string
                        description: user id
                        default: "31.01.2022"
                    period:
                        type: integer
                        description: period 1 to 60
                        default: 3
                    amount:
                        type: integer
                        description: amount from 10000 to 3000000
                        default: 10000
                    rate:
                        type: number
                        description: from 1 to 8
                        default: 6
"""
    data = request.json
    try:
        return jsonify(dict_data_base(data['date'], data['period'], data['amount'], data['rate']))
    except KeyError:
        abort(400, description="request неполный, отсутствует один из ключей")
    except TypeError:
        abort(400, description="request неполный, отсутствует один из ключей")



app.config['JSON_AS_ASCII'] = False
app.config['TESTING'] = True

swagger = Swagger(app)
test_client = app.test_client()
test_client.testing = True


if __name__ == "__main__":
   app.run(debug=True)