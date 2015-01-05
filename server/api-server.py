"""
requests:
http://localhost:5000/api/v1.0/<main_function>/<sub_function>/



@brief          checks email, password and crate a session
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
    return json.dumps({'userId': userId, 'email': user_name})

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
        if( f[0] == mainFunction  ):
            bAuthorityError = checkAuthority( mainFunction, subFunction )
            if( bAuthorityError == 0 ):
                return f[1]( subFunction )
            else:
                return HandleError( bAuthorityError )
            
    return abort(404)
def checkAuthority(m,s):
    #m = mainFunction
    #s = subFunction
    if( not 'email' in sessions ):
        return 10005 #Requires authentication
    return 0 # we need "permissions" table for checking
def account(subFunction):
    func_list = [("login",account_login),("register",account_register), ("logout",account_logout)]
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
def account_register():
#test: curl -i -H "Content-Type: application/json" -X GET -d "{"""u_name""":"""test12""","""u_surname""":"""test3""","""u_mail""":"""test3""","""u_pass""":"""test3""","""u_phone""":"""test3""","""u_facebookid""":"""test3"""}" http://localhost:5000/api/v1.0/account/register/

    if( not 'u_name' in request.json or
       not 'u_surname' in request.json or
       not 'u_mail' in request.json or
       not 'u_pass' in request.json or
       not 'u_phone' in request.json or
       not 'u_facebookid' in request.json ):
        return HandleError( 1002 )    
    u_name = request.json['u_name']
    u_surname = request.json['u_surname']
    u_mail = request.json['u_mail']
    u_pass = request.json['u_pass']
    u_phone = request.json['u_phone']
    u_facebookid = request.json['u_facebookid']
    import register
    res = register.register(u_name,u_surname,u_mail,u_pass,str(u_phone),u_facebookid)
    if( res == True ):
        return jsonify( { 'register': "True" } ), 201
    else:
        return jsonify( { 'register': "False" } ), 201
    
def account_login():
    
    if( not 'email' in request.json or
       not 'password' in request.json):
        return HandleError( 1002 )
    
    email = request.json['email']
    password = request.json['password']
    if( len(email) == 0 or
        len(password) == 0):
        return HandleError( 1000 )
        
        
    import login
    res = login.login(email,password)
    if( res == True ):
        session['email'] = email
        return jsonify( { 'login': "True" } ), 201
    else:
        return jsonify( { 'login': "False" } ), 201

def account_logout():
    session.pop('email', None)
    

def HandleError( dest_error ):
    return jsonify( { 'error': dest_error } ), 201


if __name__ == '__main__':
    flask_app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT' #secret?
    flask_app.run(debug=True)
