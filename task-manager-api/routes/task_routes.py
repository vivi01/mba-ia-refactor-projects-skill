from flask import Blueprint, request, jsonify
from database import db
from models.task import Task
from sqlalchemy.orm import joinedload
from datetime import datetime

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    # Resolvendo AP-003: Eager Loading com joinedload para evitar N+1
    tasks = db.session.query(Task).options(joinedload(Task.user), joinedload(Task.category)).all()
    # Resolvendo AP-002: Lógica delegada ao Model (to_dict)
    return jsonify([t.to_dict() for t in tasks]), 200

@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Resolvendo AP-004: Usando session.get
    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({'error': 'Task não encontrada'}), 404
    return jsonify(task.to_dict()), 200

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Título é obrigatório'}), 400

    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        status=data.get('status', 'pending'),
        priority=data.get('priority', 3),
        user_id=data.get('user_id'),
        category_id=data.get('category_id')
    )

    if data.get('due_date'):
        try:
            task.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Formato de data inválido (YYYY-MM-DD)'}), 400

    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({'error': 'Task não encontrada'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Deletada com sucesso'}), 200
