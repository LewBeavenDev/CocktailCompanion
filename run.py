import os
from thecocktailcompanion import create_app

app = create_app()

if __name__ == '__main__':
    # This section only runs the app in a development environment
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable or default to 5000
    app.run(host="0.0.0.0", port=port)
