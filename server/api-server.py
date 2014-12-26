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
def not_found(error = 404):
    return make_response(jsonify( { 'error': 'request not found' } ), 404)


@flask_app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@flask_app.route('/api/v1.0/<string:mainFunction>/<string:subFunction>/')
def APIStart( mainFunction, subFunction ):
    
    func_list = [("account",account),("organization",organization)]
    for f in func_list:
        if( f[0] == mainFunction ):
            return f[1]( subFunction )
            
    return not_found()


def account(subFunction):
    func_list = [("login",t_function),("register",t_function), ("logout",t_function)]
    for f in func_list:
        if( f[0] == subFunction ):
            return f[1]()
    return not_found()
    
def organization(subFunction):
    func_list = [("create",t_function),("delete",t_function), ("update",t_function)]
    for f in func_list:
        if( f[0] == subFunction ):
            return f[1]()
    return not_found()
def t_function():
    return "still has a lot of things to do."
if __name__ == '__main__':
    flask_app.run(debug=True)
