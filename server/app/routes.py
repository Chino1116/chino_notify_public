from flask import Blueprint, request, jsonify
from .models import db, Message

api_bp = Blueprint('api', __name__)

# Token验证装饰器
def require_token(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        expected_token = 'your-token'
        if not token or token != f"Bearer {expected_token}":
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

@api_bp.route('/webhook', methods=['POST'])
@require_token
def webhook():
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    message = Message(title=data['title'], content=data['content'])
    db.session.add(message)
    db.session.commit()

    total_messages = Message.query.count()
    return jsonify({'message': 'Notification received', 'id': total_messages}), 201

@api_bp.route('/messages', methods=['GET'])
@require_token
def get_messages():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    result = []
    for i, msg in enumerate(messages, start=1):
        msg_dict = msg.to_dict()
        msg_dict['id'] = i
        result.append(msg_dict)
    return jsonify(result)

@api_bp.route('/messages/<int:id>', methods=['DELETE'])
@require_token
def delete_message(id):
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    if id < 1 or id > len(messages):
        return jsonify({'error': 'Invalid ID'}), 404
    message = messages[id - 1]
    db.session.delete(message)
    db.session.commit()
    return jsonify({'message': 'Message deleted'})

@api_bp.route('/messages', methods=['DELETE'])
@require_token
def delete_messages():
    display_ids = request.get_json().get('ids', [])
    if not display_ids:
        return jsonify({'error': 'No IDs provided'}), 400

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    to_delete = []
    for did in display_ids:
        if did < 1 or did > len(messages):
            return jsonify({'error': f'Invalid ID {did}'}), 400
        to_delete.append(messages[did - 1])
    
    for msg in to_delete:
        db.session.delete(msg)
    db.session.commit()
    return jsonify({'message': f'Deleted {len(to_delete)} messages'})

# 标记消息为已查看
@api_bp.route('/messages/visited', methods=['POST'])
@require_token
def mark_visited():
    data = request.get_json()
    display_ids = data.get('ids', [])
    visited = data.get('visited', True)
    
    if not display_ids:
        return jsonify({'error': 'No IDs provided'}), 400

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    updated = []
    for did in display_ids:
        if did < 1 or did > len(messages):
            return jsonify({'error': f'Invalid ID {did}'}), 400
        messages[did - 1].visited = visited
        updated.append(did)
    
    db.session.commit()
    return jsonify({'message': f'Updated {len(updated)} messages', 'ids': updated})
