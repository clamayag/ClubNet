#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: ClubNet
#-----------------------------------------------------------------------

import sqlalchemy.ext.declarative
import sqlalchemy
import os
from datetime import datetime

Base = sqlalchemy.ext.declarative.declarative_base()
#-----------------------------------------------------------------------
class User (Base):
    __tablename__ = 'users'
    user_id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    profile_image_url = sqlalchemy.Column(sqlalchemy.String)
    class_year = sqlalchemy.Column(sqlalchemy.Integer)
    major = sqlalchemy.Column(sqlalchemy.String)
    team_position = sqlalchemy.Column(sqlalchemy.String)
    favorite_team = sqlalchemy.Column(sqlalchemy.String)
    hometown = sqlalchemy.Column(sqlalchemy.String)
    job_title = sqlalchemy.Column(sqlalchemy.String)
    user_company = sqlalchemy.Column(sqlalchemy.String)

#-----------------------------------------------------------------------

class Users_Clubs (Base):
    __tablename__ = 'user_club_id'
    username = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    club_id = sqlalchemy.Column(sqlalchemy.Integer)

#-----------------------------------------------------------------------

class Posts(Base):
    __tablename__ = 'posts'
    post_id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement = True, primary_key = True)
    club_image_url = sqlalchemy.Column(sqlalchemy.String)
    creator_id = sqlalchemy.Column(sqlalchemy.String)
    title = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    timestamp = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True))

#-----------------------------------------------------------------------
class Requests(Base):
    __tablename__ = 'requests'
    request_timestamp = sqlalchemy.Column(sqlalchemy.DateTime(timezone=False), primary_key = True)
    club_id = sqlalchemy.Column(sqlalchemy.Integer)
    user_id = sqlalchemy.Column(sqlalchemy.String)

#-----------------------------------------------------------------------

def init_database():
    CLUB_SOCC = 1
    DATABASE_URL = os.getenv('DB_URL')
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

    engine = sqlalchemy.create_engine(DATABASE_URL)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with sqlalchemy.orm.Session(engine) as session:
        user1 = User(user_id = "allenwu",
                    name = "Allen Wu",
                    email = "allenwu@princeton.edu",
                    profile_image_url = "https://picsum.photos/500/500")
        session.add(user1)
        user2 = User(user_id = "renteria",
                    name = "Emilio Cano",
                    email = "emiliocanor@princeton.edu",
                    profile_image_url = "https://picsum.photos/500/500")
        session.add(user2)
        user3 = User(user_id = "yparikh",
                    name = "Yash Parikh",
                    email = "yparikh@princeton.edu",
                    profile_image_url = "https://picsum.photos/500/500")
        session.add(user3)

        user_clubs1 = Users_Clubs(username = 'allenwu',
                                    club_id = CLUB_SOCC)
        session.add(user_clubs1)
        user_clubs2 = Users_Clubs(username = 'yparikh',
                                    club_id = CLUB_SOCC)
        session.add(user_clubs2)
        user_clubs3 = Users_Clubs(username = 'oguntola',
                                    club_id = CLUB_SOCC)
        session.add(user_clubs3)
        user_clubs4 = Users_Clubs(username = 'renteria',
                                    club_id = CLUB_SOCC)
        session.add(user_clubs4)
        post1 = Posts(creator_id = "yparikh",
                    title = "hello",
                    description = "world")
        session.add(post1)
        # req1 = Requests(user_id = "yparikh",
        #             request_timestamp = datetime.now(),
        #             club_id = CLUB_SOCC)
        # session.add(req1)
        session.commit()


if __name__ == '__main__':
    init_database()
