from api.database.database import db
from api.models.models import User, Post, Comment, Notif


def create_test_data():

    # ######## USER ########
    # users = User.query.all()
    # for user in users:
    #     user.image_file = '/img/default.png'
    #     db.session.add(user)
    #     db.session.commit()

    # # for i in range(6,10):

    #     user = User(
    #         username=f"investorqual{i}",
    #         password=f"investorqual{i}",
    #         accuracy=i*9,
    #         email=f"investorqual{i}@investorqual.com",
    #         stocks="AAPL MSFT GAZP",
    #         role="investorqual",
    #     )

    #     db.session.add(user)
    #     db.session.commit()

    # ######## POST ########
    # post = Post.query.filter_by(pid="1").first()
    # text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    # sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
    # nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
    # reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
    # mollit anim id est laborum."""

    # users = User.query.all()
    # for user in users:
    #     post = Post(content=text, media="Test Media", user_id=user.uid)
    #     db.session.add(post)
    #     db.session.commit()

    # ######## Comment ########
    # comment = Comment.query.filter_by(cid="1").first()

    # if comment is None:
    #     comment = Comment(content="Test Comment", post_id=1, user_id=1)
    #     db.session.add(comment)
    #     db.session.commit()

    # ######## Notif ########
    # notif = Notif.query.filter_by(nid="1").first()

    # if notif is None:
    #     notif = Notif(msg="Test Notif", post_id=1, for_uid=1, author="Test Author")
    #     db.session.add(notif)
    #     db.session.commit()
    pass