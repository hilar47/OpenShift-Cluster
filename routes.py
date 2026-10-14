"""Routes for the counter service."""
from flask import jsonify, abort

from service import app

COUNTERS = {}


@app.route("/")
def index():
    """Return service info."""
    return jsonify(name="Counter Service", version="1.0"), 200


@app.route("/health")
def health():
    """Return health status."""
    return jsonify(status="OK"), 200


@app.route("/counters", methods=["GET"])
def list_counters():
    """List all counters."""
    return jsonify(COUNTERS), 200


@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """Create a counter starting at 0."""
    if name in COUNTERS:
        abort(409, description=f"Counter {name} already exists")
    COUNTERS[name] = 0
    return jsonify({name: COUNTERS[name]}), 201


@app.route("/counters/<name>", methods=["GET"])
def read_counter(name):
    """Read a counter."""
    if name not in COUNTERS:
        abort(404, description=f"Counter {name} not found")
    return jsonify({name: COUNTERS[name]}), 200


@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    """Increment a counter."""
    if name not in COUNTERS:
        abort(404, description=f"Counter {name} not found")
    COUNTERS[name] += 1
    return jsonify({name: COUNTERS[name]}), 200


@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    """Delete a counter."""
    COUNTERS.pop(name, None)
    return "", 204
