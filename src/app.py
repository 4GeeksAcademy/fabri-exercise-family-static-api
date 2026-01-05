import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


jackson_family = FamilyStructure("Jackson")



@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code



@app.route("/")
def sitemap():
    return generate_sitemap(app)



@app.route("/members", methods=["GET"])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200



@app.route("/members/<int:member_id>", methods=["GET"])
def get_one_member(member_id):
    member = jackson_family.get_member(member_id)

    if member is None:
        return jsonify({"error": "Member not found"}), 404

    return jsonify(member), 200



@app.route("/members", methods=["POST"])
def create_member():
    data = request.get_json(silent=True)

   
    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    try:
        created = jackson_family.add_member(data)
        return jsonify(created), 200
    except ValueError as e:
        
        return jsonify({"error": str(e)}), 400
    except Exception:
        
        return jsonify({"error": "Internal server error"}), 500



@app.route("/members/<int:member_id>", methods=["DELETE"])
def delete_member(member_id):
    deleted = jackson_family.delete_member(member_id)

    if not deleted:
        return jsonify({"error": "Member not found"}), 404

    return jsonify({"done": True}), 200



if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=PORT, debug=True)