#!/usr/bin/python3
"""
States view
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET", "POST"])
def states_endpoint():
    """
    Handles post and get req to /states
    """
    if request.method == "POST":
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        if req_json.get("name") is None:
            abort(400, 'Missing name')

        new_obj = State(**req_json)
        new_obj.save()
        return jsonify(new_obj.to_json()), 201
    if request.method == "GET":
        all_states = storage.all("State")
        all_states = list(obj.to_json() for obj in all_states.values())
        return jsonify(all_states)


@app_views.route("/states/<state_id>", methods=['GET', 'PUT', 'DELETE'])
def state_by_id(state_id):
    """
    Handels GET, PUT and DELETE on a single state
    """
    state_obj = storage.get("State", state_id)
    if state_obj is None:
        abort(404, 'Not found')

    if request.method == "GET":
        return jsonify(state_obj.to_json())

    if request.method == 'DELETE':
        state_obj.delete()
        del state_obj
        return jsonify({})

    if request.method == 'PUT':
        req_json = request.get_json()
        if req_json is None:
            abort(400, "Not a JSON")

        state_obj.bm_update(req_json)
        return jsonify(state_obj.to_json())
