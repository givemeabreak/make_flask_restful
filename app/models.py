from app.extentions import db


class User(db.Model):
    uid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    uname = db.Column(db.String(16),unique=True)
    upassword = db.Column(db.String(256))

    def save(self):
        db.session.add(self)
        db.session.commit()