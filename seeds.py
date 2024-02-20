from app.models import User, Post, Comment, Vote
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
users = [
    User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
    User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
    User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
    User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
    User(username='djiri4', email='gmidgley4@weather.com', password='password123')
]
db.add_all(users)
db.commit()

# insert posts
posts = [
    Post(title='Donec posuere metus vitae ipsum', post_url='https://buzzfeed.com/in/imperdiet/et/commodo/vulputate.png', user_id=1),
    Post(title='Morbi non quam nec dui luctus rutrum', post_url='https://nasa.gov/donec.json', user_id=1),
    Post(title='Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue', post_url='https://europa.eu/parturient/montes/nascetur/ridiculus/mus/etiam/vel.aspx', user_id=2),
    Post(title='Nunc purus', post_url='http://desdev.cn/enim/blandit/mi.jpg', user_id=3),
    Post(title='Pellentesque eget nunc', post_url='http://google.ca/nam/nulla/integer.aspx', user_id=4)
]
db.add_all(posts)
db.commit()

# insert comments
comments = [
    Comment(text='Nunc rhoncus dui vel sem.', user_id=1, post_id=2),
    Comment(text='Nunc rhoncus dui vel sem.', user_id=2, post_id=3),
    Comment(text='Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.', user_id=1, post_id=3),
    Comment(text='Aliquam erat volutpat. In congue.', user_id=2, post_id=1),
    Comment(text='Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.', user_id=2, post_id=3),
    Comment(text='In hac habitasse platea dictumst.', user_id=3, post_id=3)
]
db.add_all(comments)
db.commit()

# insert votes
votes = [
    Vote(user_id=1, post_id=2),
    Vote(user_id=1, post_id=4),
    Vote(user_id=2, post_id=4),
    Vote(user_id=3, post_id=4),
    Vote(user_id=4, post_id=2)
]
db.add_all(votes)
db.commit()

db.close()
