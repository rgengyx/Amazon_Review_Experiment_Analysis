# Python Packages

# 3rd Party Packages
from flask import Flask
from flask import render_template
from flask_cors import CORS, cross_origin

# Self-defined Packages and Modules
from api.UserAPI import user_api
from api.ProductAPI import product_api

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Enable CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['Cache-Control'] = 'public, max-age=0'
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route("/")
def render_index():
    return render_template('index.html')

@app.route("/description")
def render_description():
    return render_template('description.html')

@app.route("/instruction")
def render_instruction():
    return render_template('instruction.html')

@app.route("/product")
def render_product():
    return render_template('product.html')

@app.route("/thankyou")
def render_thankyou():
    return render_template('thankyou.html')

# API endpoints
app.register_blueprint(user_api, url_prefix='/api')
app.register_blueprint(product_api, url_prefix='/api')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
