from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.Text, nullable=False)
    split_sentence = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.String(10), nullable=True)
    datetime = db.Column(db.String(20), nullable=False)
    train_dev_test = db.Column(db.String(10), nullable=False)
    
    writer_joy = db.Column(db.Integer, nullable=False)
    writer_sadness = db.Column(db.Integer, nullable=False)
    writer_anticipation = db.Column(db.Integer, nullable=False)
    writer_surprise = db.Column(db.Integer, nullable=False)
    writer_anger = db.Column(db.Integer, nullable=False)
    writer_fear = db.Column(db.Integer, nullable=False)
    writer_disgust = db.Column(db.Integer, nullable=False)
    writer_trust = db.Column(db.Integer, nullable=False)
    writer_sentiment = db.Column(db.Integer, nullable=False)

    reader1_joy = db.Column(db.Integer, nullable=False)
    reader1_sadness = db.Column(db.Integer, nullable=False)
    reader1_anticipation = db.Column(db.Integer, nullable=False)
    reader1_surprise = db.Column(db.Integer, nullable=False)
    reader1_anger = db.Column(db.Integer, nullable=False)
    reader1_fear = db.Column(db.Integer, nullable=False)
    reader1_disgust = db.Column(db.Integer, nullable=False)
    reader1_trust = db.Column(db.Integer, nullable=False)
    reader1_sentiment = db.Column(db.Integer, nullable=False)

    reader2_joy = db.Column(db.Integer, nullable=False)
    reader2_sadness = db.Column(db.Integer, nullable=False)
    reader2_anticipation = db.Column(db.Integer, nullable=False)
    reader2_surprise = db.Column(db.Integer, nullable=False)
    reader2_anger = db.Column(db.Integer, nullable=False)
    reader2_fear = db.Column(db.Integer, nullable=False)
    reader2_disgust = db.Column(db.Integer, nullable=False)
    reader2_trust = db.Column(db.Integer, nullable=False)
    reader2_sentiment = db.Column(db.Integer, nullable=False)

    reader3_joy = db.Column(db.Integer, nullable=False)
    reader3_sadness = db.Column(db.Integer, nullable=False)
    reader3_anticipation = db.Column(db.Integer, nullable=False)
    reader3_surprise = db.Column(db.Integer, nullable=False)
    reader3_anger = db.Column(db.Integer, nullable=False)
    reader3_fear = db.Column(db.Integer, nullable=False)
    reader3_disgust = db.Column(db.Integer, nullable=False)
    reader3_trust = db.Column(db.Integer, nullable=False)
    reader3_sentiment = db.Column(db.Integer, nullable=False)

    avg_readers_joy = db.Column(db.Integer, nullable=False)
    avg_readers_sadness = db.Column(db.Integer, nullable=False)
    avg_readers_anticipation = db.Column(db.Integer, nullable=False)
    avg_readers_surprise = db.Column(db.Integer, nullable=False)
    avg_readers_anger = db.Column(db.Integer, nullable=False)
    avg_readers_fear = db.Column(db.Integer, nullable=False)
    avg_readers_disgust = db.Column(db.Integer, nullable=False)
    avg_readers_trust = db.Column(db.Integer, nullable=False)
    avg_readers_sentiment = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Annotation {self.sentence[:20]}...>'
