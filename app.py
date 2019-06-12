"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
   # json_data = {'Hello': 'World!'}
   # return ปณิตา 8 4/1
     return 

if __name__ == '__main__':
    app.run()
