"""Script para popular o banco com dados iniciais (Refatorado para MVC)"""
from app import create_app, db
from models.task import Task
from models.user import User
from models.category import Category
from datetime import datetime, timedelta

def seed_data():
    app = create_app()
    with app.app_context():
        # Limpar dados antigos
        db.session.query(Task).delete()
        db.session.query(User).delete()
        db.session.query(Category).delete()
        db.session.commit()

        # Criar Usuários
        u1 = User(name='João Silva', email='joao@email.com', role='admin')
        u1.set_password('1234')
        u2 = User(name='Maria Santos', email='maria@email.com', role='user')
        u2.set_password('abcd')
        u3 = User(name='Pedro Oliveira', email='pedro@email.com', role='manager')
        u3.set_password('pass')
        
        db.session.add_all([u1, u2, u3])
        db.session.commit()

        # Criar Categorias
        c1 = Category(name='Backend', description='Tarefas de backend', color='#3498db')
        c2 = Category(name='Frontend', description='Tarefas de frontend', color='#2ecc71')
        c3 = Category(name='DevOps', description='Tarefas de infraestrutura', color='#e74c3c')
        c4 = Category(name='Bug', description='Correção de bugs', color='#e67e22')
        
        db.session.add_all([c1, c2, c3, c4])
        db.session.commit()

        # Criar Tasks
        tasks_data = [
            {'title': 'Implementar autenticação JWT', 'description': 'Adicionar autenticação real com JWT', 'status': 'pending', 'priority': 1, 'user_id': u1.id, 'category_id': c1.id, 'due_date': datetime.utcnow() - timedelta(days=3)},
            {'title': 'Criar tela de login', 'description': 'Tela de login responsiva', 'status': 'in_progress', 'priority': 2, 'user_id': u2.id, 'category_id': c2.id, 'due_date': datetime.utcnow() + timedelta(days=5)},
            {'title': 'Configurar CI/CD', 'description': 'Pipeline com GitHub Actions', 'status': 'done', 'priority': 2, 'user_id': u3.id, 'category_id': c3.id, 'tags': 'devops,ci,github'},
        ]

        for td in tasks_data:
            t = Task(**td)
            db.session.add(t)

        db.session.commit()
        print("Seed concluído com sucesso!")
        print(f"  {db.session.query(User).count()} usuários")
        print(f"  {db.session.query(Task).count()} tasks")

if __name__ == '__main__':
    seed_data()
