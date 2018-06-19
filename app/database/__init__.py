from ..database.models import User, Role, Post, Category
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


def init_data():
    db.drop_all()
    db.create_all()

    roleAdmin = Role(role="admin")
    db.session.add(roleAdmin)
    roleUser = Role(role="user")
    db.session.add(roleUser)
    db.session.commit()

    category1 = Category(category_name="Technology")
    category2 = Category(category_name="Sc-Fi")
    db.session.add_all([category1, category2])
    db.session.commit()

    for i in range(1, 20):
        hashed_password = generate_password_hash("p" + str(i), method="sha256")
        if i % 2 != 0:
            user = User(username="tom" + str(i), email="tom" +
                        str(i) + "@tom.pl", password=hashed_password, role=roleAdmin)
            db.session.add(user)
        else:
            user = User(username="tom" + str(i), email="tom" +
                        str(i) + "@tom.pl", password=hashed_password, role=roleUser)
            db.session.add(user)

    db.session.commit()

    for i in range(1, 30):

        if i % 2 != 0:
            post = Post(title="Some title " + str(i), content="Some content " +
                        str(1), author="Tom4", category=category1)
        else:
            post = Post(title="Some title " + str(i), content="Some content " +
                        str(1), author="Tom4", category=category2)

        db.session.add(post)

    db.session.commit()


# init_data() 
