from app import app
from app import settings

if __name__ == "__main__":  
    app.run(debug=settings.FLASK_DEBUG, port=settings.PORT) 