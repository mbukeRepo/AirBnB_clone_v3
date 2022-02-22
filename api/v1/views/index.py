#!/usr/bin/python3
"""
handles /status and /stats routes
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """
    function for status route
    handles: /status
    """
    if request.method == 'GET':
        return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    returns total of each entity
    handles: /stats
    """
    if request.method == 'GET':
        stats = {"amenities": "Amenity",
                 "cities": "City",
                 "places": "Place",
                 "reviews": "Review",
                 "states": "State",
                 "users": "User"}
        for k, v in stats.items():
            stats[k] = storage.count(v)

        return jsonify(stats)
