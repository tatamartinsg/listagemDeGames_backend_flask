from flask import Flask, make_response, jsonify, request

app = Flask(__name__)


from website.controllers import games

