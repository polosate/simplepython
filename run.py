from app import app
from app.handler import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5090, debug=True)