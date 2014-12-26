"""
requests:
http://localhost:5000/api/v1.0/<main_function>/<sub_function>/


http://localhost:5000/api/v1.0/account/login
http://localhost:5000/api/v1.0/account/logout
http://localhost:5000/api/v1.0/account/register

http://localhost:5000/api/v1.0/organization/create
http://localhost:5000/api/v1.0/organization/delete
http://localhost:5000/api/v1.0/organization/update


ex:
curl -i -H "Content-Type: application/json" -d '{"tag":"data.."}' http://localhost:5000/...


"""

from flask import Flask, jsonify, abort, request, make_response, url_for

flask_app = Flask(__name__)

@flask_app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'request not found' } ), 404)
@flask_app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@flask_app.route('/api/v1.0/<string:mainFunction>/<string:subFunction>')
def APIStart( mainFunction, subFunction ):
    print mainFunction + " " + subFunction


if __name__ == '__main__':
    flask_app.run(debug=True)
