from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

members = [{
    "id": 1,
    "name": "Shawnee Millard",
    "role": "software engineer",
    "level": "junior"
},
    {
        "id": 2,
        "name": "Kendall Kennith",
        "role": "software engineer",
        "level": "middle"
    },
    {
        "id": 3,
        "name": "Mavis Derek",
        "role": "software engineer",
        "level": "senior"
    },
    {
        "id": 4,
        "name": "Krystal Dolores",
        "role": "QA engineer",
        "level": "middle"
    }
]


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify({'team_members': members})

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = [member for member in members if member['id'] == member_id]
    if len(member) == 0: abort(404)
    return jsonify(member[0])

if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)

	
	'''
	jhgjhgjhg
	'''