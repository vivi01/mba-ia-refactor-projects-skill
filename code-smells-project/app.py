import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from routes import api_bp
from database import get_db

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configurações
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "chave-padrao-segura")
    app.config["DEBUG"] = os.getenv("DEBUG", "False").lower() == "true"
    
    CORS(app)
    
    # Registro de Rotas (MVC)
    app.register_blueprint(api_bp)

    @app.route("/")
    def index():
        return jsonify({
            "mensagem": "API da Loja Refatorada (MVC)",
            "status": "online"
        })

    # Centralized Error Handling (AP-003)
    @app.errorhandler(Exception)
    def handle_exception(e):
        """Captura todas as exceções não tratadas e retorna um erro JSON padronizado."""
        # Se for um erro conhecido (ex: ValueError do Model), retorna 400
        if isinstance(e, ValueError):
            return jsonify({"erro": str(e), "sucesso": False}), 400
            
        # Para outros erros, retorna 500
        response = {
            "erro": "Erro interno do servidor",
            "detalhes": str(e) if app.debug else "Ocorreu um erro inesperado",
            "sucesso": False
        }
        return jsonify(response), 500

    return app

if __name__ == "__main__":
    app = create_app()
    
    with app.app_context():
        get_db() # Inicializa banco

    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
