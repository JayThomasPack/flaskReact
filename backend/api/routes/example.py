# In api/routes/example.py
from flask import jsonify
from .. import api

@api.route('/example', methods=['GET'])
def get_example():
    return jsonify({'message': 'This is an example endpoint'})
