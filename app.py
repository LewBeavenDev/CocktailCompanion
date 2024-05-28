import os
from thecocktailcompanion import app

# Set default port if not provided in environment variables
port = int(os.environ.get("PORT", 5000))
host = os.environ.get("IP", "0.0.0.0")

if __name__ == "__main__":
    app.run(
        host=host,
        port=port,
        debug=True
    )
