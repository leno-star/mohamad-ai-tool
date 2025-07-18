from flask import Flask
from backend.routes.generate import generate_bp
from backend.routes.feedback import feedback_bp
from backend.routes.regenerate import regenerate_bp
from backend.routes.vip_session import vip_bp

app = Flask(__name__)

# تسجيل نقاط الـ API
app.register_blueprint(generate_bp)
app.register_blueprint(feedback_bp)
app.register_blueprint(regenerate_bp)
app.register_blueprint(vip_bp)

if __name__ == '__main__':
    app.run(debug=True)