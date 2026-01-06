from . import db
from datetime import datetime, timezone

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    visited = db.Column(db.Boolean, default=False, nullable=False)

    def to_dict(self):
        # 确保时间戳明确标示为 UTC（添加 Z 后缀）
        # Python datetime.utcnow() 返回的是 naive datetime，需要添加 UTC 标记
        timestamp_str = self.timestamp.replace(tzinfo=timezone.utc).isoformat()
        
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'timestamp': timestamp_str,  # 返回带 Z 的 UTC 时间，例如：2026-01-05T10:30:45+00:00
            'visited': self.visited
        }
