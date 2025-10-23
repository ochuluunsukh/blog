from fastapi import FastAPI
from faker import Faker
import random
from sqlalchemy.orm import Session
from app import models, utils
from app.database import engine, SessionLocal

# FastAPI instance
app = FastAPI()

fake = Faker("en_US")

models.Base.metadata.create_all(bind=engine)


def create_fake_users(db: Session, num_users: int = 3):
    if db.query(models.User).count() > 0:
        print("user data already exists, skipping seeding.")
        return

    users_to_add = []
    for _ in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name}.{last_name}{random.randint(1, 99)}@{fake.domain_name()}".lower()
        password = "password123"
        hashed_password = utils.hash(password)
        user = models.User(
            email=email,
            password=hashed_password,
        )
        users_to_add.append(user)

    db.add_all(users_to_add)

    db.commit()
    print(f"✅ {num_users} fake users have been successfully added.")


def create_fake_posts(db: Session, num_posts: int = 10):
    if db.query(models.Post).count() > 0:
        print("Post data already exists, skipping seeding.")
        return

    user_ids = [user.id for user in db.query(models.User.id).all()]

    if not user_ids:
        print("No users found. Please create users before adding posts.")
        return

    posts_to_add = []

    for _ in range(num_posts):
        title = fake.sentence(nb_words=6)
        content = fake.text(max_nb_chars=50)
        published = fake.boolean(chance_of_getting_true=90)

        owner_id = random.choice(user_ids)

        post = models.Post(
            title=title,
            content=content,
            published=published,
            owner_id=owner_id,
        )
        posts_to_add.append(post)

    db.add_all(posts_to_add)
    db.commit()
    print(f"✅ {num_posts} fake posts have been successfully added.")


def create_fake_votes(db: Session, max_votes: int = 50):
    if db.query(models.Vote).count() > 0:
        print("Vote-ын хүснэгтэд өгөгдөл байгаа тул нэмсэнгүй.")
        return

    # 2. Одоо байгаа User болон Post-ын ID-г татаж авах
    user_ids = [user.id for user in db.query(models.User.id).all()]
    post_ids = [post.id for post in db.query(models.Post.id).all()]

    if not user_ids or not post_ids:
        print(
            "Vote and Post data are required to create votes. Please add dummy data for them first."
        )
        return

    existing_combinations = set()

    votes_to_add = []

    # randomly generate unique user-post vote combinations
    num_users = len(user_ids)
    num_posts = len(post_ids)
    max_possible_votes = num_users * num_posts

    # Limit the number of votes to create
    votes_to_create = min(max_votes, max_possible_votes)

    i = 0
    while len(votes_to_add) < votes_to_create and i < max_possible_votes * 2:
        random_user_id = random.choice(user_ids)
        random_post_id = random.choice(post_ids)

        combination = (random_user_id, random_post_id)

        if combination not in existing_combinations:
            vote = models.Vote(user_id=random_user_id, post_id=random_post_id)
            votes_to_add.append(vote)
            existing_combinations.add(combination)

        i += 1

        if len(existing_combinations) == max_possible_votes:
            break

    db.add_all(votes_to_add)
    db.commit()
    print(f"✅ {len(votes_to_add)} fake votes have been successfully added.")


if __name__ == "__main__":
    with SessionLocal() as db:
        create_fake_users(db)
        create_fake_posts(db)
        create_fake_votes(db)
