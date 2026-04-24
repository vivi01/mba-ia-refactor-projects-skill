import os
from flask import Flask, jsonify
from flask_cors import CORS
from database import db
from routes.task_routes import task_bp
from routes.user_routes import user_bp
from routes.report_routes import report_bp
from dotenv import load_dotenv

# Carrega .env
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configurações via Env (AP-001/AP-002 fix)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///tasks.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')

    CORS(app)
    db.init_app(app)

    # Registro de Blueprints
    app.register_blueprint(task_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(report_bp)

    @app.route('/health')
    def health():
        return jsonify({'status': 'ok', 'env': os.getenv('NODE_ENV', 'development')})

    @app.route('/')
    def index():
        return jsonify({'message': 'Task Manager API Refatorada (MVC)', 'version': '2.0'})

    # Error Handling Global
    @app.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if hasattr(e, 'code'): code = e.code
        return jsonify({'error': str(e), 'success': False}), code

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
