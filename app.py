from flask import Flask, render_template, request, redirect

from flask_migrate import Migrate
from models import Post, Comment, db
import datetime

app = Flask(__name__)
# FlaskアプリケーションとSQLAlchemyを紐付ける
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
# Flask-Migrateをインスタンス化する
migrate = Migrate(app, db)

# トップページ用のルーティング
@app.route('/')
def index():
    # 投稿を全て取得する
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['POST'])
def create():
    # フォームから送信された情報を取得
    name = request.form['name']
    text = request.form['text']
    # 現在時刻を取得
    now = datetime.datetime.now()
    # 新しい投稿を作成
    post = Post(name=name, text=text, time=now)
    # 投稿をデータベースに保存
    db.session.add(post)
    db.session.commit()
    # トップページにリダイレクト
    return redirect('/')


# 投稿詳細用のルーティング
@app.route('/post/<int:id>', methods=['GET'])
def post_detail(id):
    # 投稿を取得
    post = Post.query.get(id)
    # コメントを取得
    comments = Comment.query.filter_by(post_id=id).all()
    return render_template('post_detail.html', post=post, comments=comments)

# コメント作成用のルーティング
@app.route('/post/<int:id>/create', methods=['POST'])
def create_comment(id):
    # フォームから送信された情報を取得
    name = request.form['name']
    text = request.form['text']
    # 現在時刻を取得
    now = datetime.datetime.now()
    # 新しいコメントを作成
    comment = Comment(name=name, text=text, time=now, post_id=id)
    # コメントを追加
    db.session.add(comment)
    # コメントを保存
    db.session.commit()
    return redirect(f'/post/{id}')

# Flaskアプリケーションのエントリポイント
if __name__ == '__main__':
    app.run(debug=True)