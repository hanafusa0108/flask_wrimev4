from flask import Flask, render_template, url_for, current_app, redirect, request, send_file, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
import json
from models import db, Annotation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///annotations.db'  # SQLiteを使用
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# データベースのテーブルを作成
with app.app_context():
    db.create_all()

# wrimeここから
@app.route("/")
def wrime():
    return render_template("table.html")


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    data = json.load(file)

    # JSONデータをパースしてデータベースに保存
    for item in data:
        
        annotation = Annotation(
            sentence=item['Sentence'],
            split_sentence=item['Split_sentence'],
            id=item['id'],
            user_id=item['UserID'],
            datetime=item['Datetime'],
            train_dev_test=item['Train/Dev/Test'],
            writer_joy=item['Writer_Joy'],
            writer_sadness=item['Writer_Sadness'],
            writer_anticipation=item['Writer_Anticipation'],
            writer_surprise=item['Writer_Surprise'],
            writer_anger=item['Writer_Anger'],
            writer_fear=item['Writer_Fear'],
            writer_disgust=item['Writer_Disgust'],
            writer_trust=item['Writer_Trust'],
            writer_sentiment=item['Writer_Sentiment'],
            reader1_joy=item['Reader1_Joy'],
            reader1_sadness=item['Reader1_Sadness'],
            reader1_anticipation=item['Reader1_Anticipation'],
            reader1_surprise=item['Reader1_Surprise'],
            reader1_anger=item['Reader1_Anger'],
            reader1_fear=item['Reader1_Fear'],
            reader1_disgust=item['Reader1_Disgust'],
            reader1_trust=item['Reader1_Trust'],
            reader1_sentiment=item['Reader1_Sentiment'],
            reader2_joy=item['Reader2_Joy'],
            reader2_sadness=item['Reader2_Sadness'],
            reader2_anticipation=item['Reader2_Anticipation'],
            reader2_surprise=item['Reader2_Surprise'],
            reader2_anger=item['Reader2_Anger'],
            reader2_fear=item['Reader2_Fear'],
            reader2_disgust=item['Reader2_Disgust'],
            reader2_trust=item['Reader2_Trust'],
            reader2_sentiment=item['Reader2_Sentiment'],
            reader3_joy=item['Reader3_Joy'],
            reader3_sadness=item['Reader3_Sadness'],
            reader3_anticipation=item['Reader3_Anticipation'],
            reader3_surprise=item['Reader3_Surprise'],
            reader3_anger=item['Reader3_Anger'],
            reader3_fear=item['Reader3_Fear'],
            reader3_disgust=item['Reader3_Disgust'],
            reader3_trust=item['Reader3_Trust'],
            reader3_sentiment=item['Reader3_Sentiment'],
            avg_readers_joy=item['Avg. Readers_Joy'],
            avg_readers_sadness=item['Avg. Readers_Sadness'],
            avg_readers_anticipation=item['Avg. Readers_Anticipation'],
            avg_readers_surprise=item['Avg. Readers_Surprise'],
            avg_readers_anger=item['Avg. Readers_Anger'],
            avg_readers_fear=item['Avg. Readers_Fear'],
            avg_readers_disgust=item['Avg. Readers_Disgust'],
            avg_readers_trust=item['Avg. Readers_Trust'],
            avg_readers_sentiment=item['Avg. Readers_Sentiment'],
            
        )
        db.session.add(annotation)

    db.session.commit()

    return jsonify({'status': 'success'})

# モデルクラス
class Annotation(db.Model):
    __tablename__ = 'annotation'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.String(500))
    split_sentence = db.Column(db.String(1000))
    avg_readers_joy = db.Column(db.Integer, nullable=False)
    avg_readers_sadness = db.Column(db.Integer, nullable=False)
    avg_readers_anticipation = db.Column(db.Integer, nullable=False)
    avg_readers_surprise = db.Column(db.Integer, nullable=False)
    avg_readers_anger = db.Column(db.Integer, nullable=False)
    avg_readers_fear = db.Column(db.Integer, nullable=False)
    avg_readers_disgust = db.Column(db.Integer, nullable=False)
    avg_readers_trust = db.Column(db.Integer, nullable=False)
    avg_readers_sentiment = db.Column(db.Integer, nullable=False)
    # その他のフィールドも追加

    def to_dict(self):
        return {
            'id': self.id,
            'Sentence': self.sentence,
            'Split_sentence': self.split_sentence,
            'Writer_Joy': self.avg_readers_joy,
            'Writer_Sadness': self.avg_readers_sadness,
            'Writer_Anticipation': self.avg_readers_anticipation,
            'Writer_Surprise': self.avg_readers_surprise,
            'Writer_Anger': self.avg_readers_anger,
            'Writer_Fear': self.avg_readers_fear,
            'Writer_Disgust': self.avg_readers_disgust,
            'Writer_Trust': self.avg_readers_trust,
            'Writer_Sentiment': self.avg_readers_sentiment,
            # その他のフィールドも必要に応じて追加
        }

# アノテーションデータ取得（1000件ずつ表示）
@app.route('/annotations', methods=['GET'])
def get_annotations():
    page = request.args.get('page', 1, type=int)  # ページ番号を取得
    per_page = 1000  # 1ページあたりの表示件数

    # 正しいpaginateの呼び出し
    annotations = Annotation.query.paginate(page=page, per_page=per_page)

    return jsonify({
        'annotations': [annotation.to_dict() for annotation in annotations.items],
        'total': annotations.total,
        'pages': annotations.pages,
        'current_page': annotations.page
    })

@app.route('/sentence/<int:sentence_id>', methods=['GET'])
def sentence_detail(sentence_id):
    # データベースから特定のIDのアノテーションを取得
    annotation = Annotation.query.filter_by(id=sentence_id).first()

    if annotation:
        # annotationが存在すれば、データをHTMLテンプレートに渡す
        return render_template('sentence_detail.html', sentence=annotation)
    else:
        return "Sentence not found", 404

@app.route('/api/sentence/<int:sentence_id>', methods=['GET'])
def sentence_detail_to_json(sentence_id):
    # データベースから特定のIDのアノテーションを取得
    annotation = Annotation.query.filter_by(id=sentence_id).first()

    if annotation:
        # annotationが存在すれば、データをJSON形式で返す
        sentence_data = {
            'id': annotation.id,
            'sentence': annotation.sentence,
            'split_sentence': annotation.split_sentence,
            'avg_readers_sentiment': annotation.avg_readers_sentiment,
            'avg_readers_joy': annotation.avg_readers_joy,
            'avg_readers_sadness': annotation.avg_readers_sadness,
            'avg_readers_anticipation': annotation.avg_readers_anticipation,
            'avg_readers_surprise': annotation.avg_readers_surprise,
            'avg_readers_anger': annotation.avg_readers_anger,
            'avg_readers_fear': annotation.avg_readers_fear,
            'avg_readers_disgust': annotation.avg_readers_disgust,
            'avg_readers_trust': annotation.avg_readers_trust
        }
        return jsonify(sentence_data)
    else:
        return jsonify({"error": "Sentence not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)