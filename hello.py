from flask import Flask

appe = Flask(__name__)

@appe.route('/')
def index():
    return 'Hello sibaloma'