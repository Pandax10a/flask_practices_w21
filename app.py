# modules to make this work, flask for api end point, dbhelpers for connection, json for data in json
from flask import Flask, request
import dbhelpers as dh
import json
import apihelper as a

app = Flask(__name__)




@app.post('/api/client')

def add_new_client():
    username = request.json.get('username')
    password = request.json.get('password')
    is_premium = request.json.get('is_premium')

    valid_check = a.check_endpoint_info(request.json, ['username', 'password', 'is_premium'])
    if (type(valid_check)==str):
        return valid_check
    
    

    result = dh.run_statement('CALL add_new_client(?,?,?)', 
    [username, password, is_premium])

    if(type(result) == list):
        client_json = json.dumps(result, default=str)
        return client_json
    else:
        print('error, error, error ')

@app.patch('/api/client_update')

def update_client():
    username = request.json.get('username')
    old_password = request.json.get('old_password')
    new_password = request.json.get('new_password')

    valid_check = a.check_endpoint_info(request.json, ['username', 'old_password', 'new_password'])
    if (type(valid_check) == str):
        return valid_check

    result = dh.run_statement('CALL update_client(?,?,?)', 
    [username, old_password, new_password])
    if(type(result) == list):
            client_json = json.dumps(result, default=str)
            return client_json
    else:
        print('error, error, error ')





app.run(debug=True)