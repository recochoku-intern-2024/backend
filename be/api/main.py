from fastapi import FastAPI
from db import session
from db import ENGINE
from sqlalchemy import text
from model import TestUserTable, TestUser, KyakuhonTable, Kyakuhon, KyakuhonPost
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

#　ユーザー情報一覧取得
# @app.get("/test_users")
# def get_user_list():
#     users = session.query(TestUserTable).all()
#     return users

@app.get("/kyakuhon")
def get_all_kyakuhon():
    users = session.query(KyakuhonTable).all()
    return users



# ユーザー情報取得(id指定)
# @app.get("/test_users/{user_id}")
# def get_user(user_id: int):
#     user = session.query(TestUserTable).\
#         filter(TestUserTable.id == user_id).first()
#     return user

@app.get("/kyakuhon/{kyakuhon_id}")
def get_kyakuhon(kyakuhon_id: int):
    user = session.query(KyakuhonTable).\
        filter(KyakuhonTable.id == kyakuhon_id).first()
    return user

# ユーザ情報登録
# @app.post("/test_users")
# def post_user(user: TestUser):
#     db_test_user = TestUser(id=user.id,
#         name=user.name,
#                             email=user.email)
#     # print("db_test_user" + db_test_user)
#     session.add(db_test_user)
#     session.commit()
#     query = text('INSERT INTO kyakuhon (title, author, genre, price) VALUES ("ものがたり1", "田中太郎", 0, 10000)')

#     return user

# @app.post("/test_users_post")
# def post_user_test(user: TestUserPost):
#     db_test_user = TestUserPost(name=user.name,
#                             email=user.email)
#     session.add(db_test_user)
#     session.commit()
#     return user

@app.post("/add_kyakuhon")
def add_kyakuhon(kyakuhon: KyakuhonPost):
    query = text("INSERT INTO kyakuhon (title, author, genre, price) VALUES (:title, :author, :genre, :price)")

    # INSERTするデータを辞書として準備
    data = {
        "title": str(kyakuhon.title),
        "author": str(kyakuhon.author),
        "genre": int(kyakuhon.genre),
        "price": int(kyakuhon.price)
    }

    with ENGINE.connect() as connection:
        connection.execute(query, **data)
    return kyakuhon



# ユーザ情報更新
# @app.put("/test_users/{user_id}")
# def put_users(user: TestUser, user_id: int):
#     target_user = session.query(TestUserTable).\
#         filter(TestUserTable.id == user_id).first()
#     target_user.name = user.name
#     target_user.email = user.email
#     session.commit()

