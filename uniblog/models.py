from database import db 


class _Model(Model):
	class Meta:
		database = db


class User(_Model):
    class Meta:
        db_table = 'users'

    id = PrimaryKeyField(null=False)
    login = CharField(max_length=140, index=True)
    password = CharField(max_length=25)
    name = CharField(max_length=35, null=False)
    surname = CharField(max_length=35, null=False)
    contacts = TextField(null=True, default="")
    active = BooleanField(default=True)
    # roles = db.relationship('Role', secondary=role_users, backref=db.backref('user', lazy='dynamic'))