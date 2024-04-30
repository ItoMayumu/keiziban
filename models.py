# Flask-SQLAlchemyをインポート
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemyのインスタンスを作成
db = SQLAlchemy()

# 投稿を表すクラス
class Post(db.Model):
    # 投稿のID
    id = db.Column(db.Integer, primary_key=True)
    # 投稿者の名前
    name = db.Column(db.String(20), nullable=False)
    # 投稿された内容
    text = db.Column(db.String(200), nullable=False)
    # 投稿された時間
    time = db.Column(db.DateTime, nullable=False)

# コメントを表すクラス
class Comment(db.Model):
    # コメントのID
    id = db.Column(db.Integer, primary_key=True)
    # コメントが対応する投稿のID
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    # コメントを投稿した者の名前
    name = db.Column(db.String(20), nullable=False)
    # コメントの内容
    text = db.Column(db.String(200), nullable=False)
    # コメントが投稿された時間
    time = db.Column(db.DateTime, nullable=False)