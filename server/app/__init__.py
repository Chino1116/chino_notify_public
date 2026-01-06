from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import sqlite3

db = SQLAlchemy()

def migrate_database(db_path):
    """数据库迁移：自动添加新字段，不清理数据"""
    if not os.path.exists(db_path):
        return  # 数据库不存在，将由 create_all 创建
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 检查 visited 字段是否存在
    cursor.execute("PRAGMA table_info(message)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'visited' not in columns:
        # 添加 visited 字段，默认值为 False (0)
        cursor.execute("ALTER TABLE message ADD COLUMN visited BOOLEAN DEFAULT 0 NOT NULL")
        conn.commit()
        print("Database migrated: added 'visited' column")
    
    conn.close()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)

    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    with app.app_context():
        # 先执行迁移
        db_path = os.path.join(app.instance_path, 'database.db')
        migrate_database(db_path)
        # 再创建表（如果不存在）
        db.create_all()

    return app
