from api.database.database import db
from api.models.models import User, Post, Comment, Notif


def create_test_data():

    ######## USER ########
    user = User.query.filter_by(username="test_username").first()

    if user is None:
        user = User(
            username="Test Username",
            password="Test Password",
            image_file="Image File",
        )
        db.session.add(user)
        db.session.commit()

    ######## POST ########
    post = Post.query.filter_by(pid="1").first()

    if post is None:
        post = Post(content="Test Post", media="Test Media", user_id=1)
        db.session.add(post)
        db.session.commit()

    ######## Comment ########
    comment = Comment.query.filter_by(cid="1").first()

    if comment is None:
        comment = Comment(content="Test Comment", post_id=1, user_id=1)
        db.session.add(comment)
        db.session.commit()

    ######## Notif ########
    notif = Notif.query.filter_by(nid="1").first()

    if notif is None:
        notif = Notif(msg="Test Notif", post_id=1, for_uid=1, author="Test Author")
        db.session.add(notif)
        db.session.commit()
