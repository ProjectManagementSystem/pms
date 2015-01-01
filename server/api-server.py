"""
requests:
http://localhost:5000/api/v1.0/<main_function>/<sub_function>/



@brief          checks username, password and crate a session
http://localhost:5000/api/v1.0/account/login

@brief          clear the sessions
http://localhost:5000/api/v1.0/account/logout

@brienf         client registration
http://localhost:5000/api/v1.0/account/register

http://localhost:5000/api/v1.0/organization/create
http://localhost:5000/api/v1.0/organization/delete
http://localhost:5000/api/v1.0/organization/update



"""


"""
##thanks anil selim surmeli for his contributions##

@app.route('/userId/<user_id>')
def get_userId(user_id):
	user_name = get_user_name(user_id)
    return json.dumps({'userId': userId, 'userName': user_name})

##thanks anil selim surmeli for his contributions##
"""


from flask import Flask, jsonify, abort, request, make_response, url_for, session

flask_app = Flask(__name__)

@flask_app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'request not found' } ), 404)


@flask_app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@flask_app.route('/api/v1.0/<string:mainFunction>/<string:subFunction>/')
def APIStart( mainFunction, subFunction ):
    
    if not request.json:
        return HandleError(10001)
        
    func_list = [("account",account),("organization",organization)]
    for f in func_list:
        if( f[0] == mainFunction ):
            return f[1]( subFunction )
            
    return abort(404)


def account(subFunction):
    func_list = [("login",account_login),("register",t_function), ("logout",account_logout)]
    for f in func_list:
        if( f[0] == subFunction ):
            return f[1]()
    return abort(404)
    
def organization(subFunction):
    func_list = [("create",t_function),("delete",t_function), ("update",t_function)]
    for f in func_list:
        if( f[0] == subFunction ):
            return f[1]()
    return abort(404)



def t_function():
    return "still has a lot of things to do."

def account_login():
    
    
    username = request.json['username']
    password = request.json['password']
    if( len(username) == 0 or
        len(password) == 0):
        return HandleError( 1000 )
        
        
    import login
    res = login.login(username,password)
    if( res == True ):
        session['username'] = username
        return jsonify( { 'login': "True" } ), 201
    else:
        return jsonify( { 'login': "False" } ), 201

def account_logout():
    session.pop('username', None)
    

def HandleError( dest_error ):
    return jsonify( { 'error': dest_error } ), 201


if __name__ == '__main__':
    flask_app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT' #secret?
    flask_app.run(debug=True)
