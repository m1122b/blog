
# fakedata.py


from faker import Faker
from ap.models import Post, db


def generate_entries(how_many=10):
    fake = Faker()
    
    for i in range(how_many):
        post = Post(
            title=fake.sentence(),
            body='\n'.join(fake.paragraphs(15)),
            is_published=True
        )
        db.session.add(post)
    
    db.session.commit()


generate_entries(10)

