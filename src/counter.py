from flask import Flask
from . import status
app = Flask(__name__)

COUNTERS = {}

@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {"Message":f"Counter {name} already exists"}, status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED

@app.route('/counters/<name>/update', methods=['POST'])
def update_counter(name):
    app.logger.info(f"Request to update counter: {name}")
    global COUNTERS
    if name not in COUNTERS:
        return {"Message":f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND
    counterval = COUNTERS[name]
    counterval += 1
    COUNTERS[name] = counterval
    return {name: COUNTERS[name]}, status.HTTP_200_OK



@app.route('/counters/<name>/delete', methods=['POST'])
def delete_counter(name):
    app.logger.info(f"Request to delete counter: {name}")
    global COUNTERS
    if name not in COUNTERS:
        return {"Message":f"Counter {name} does not exist"}, status.HTTP_404_NOT_FOUND
    del COUNTERS[name]
    return {name: None}, status.HTTP_204_NO_CONTENT