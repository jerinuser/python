#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    data = {
        'message': 'Hello, world!'
    }
    return jsonify(data)

@app.route('/api', methods=['POST'])
def post_data():
    data = request.get_json()
    # Process the data as needed
    response = {
        'message': 'Data received successfully'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()


# In[ ]:




