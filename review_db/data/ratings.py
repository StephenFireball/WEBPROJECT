import datetime
import sqlalchemy as sql
from sqlalchemy import orm
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from .review_session import SqlAlchemyBase


class Rating(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'comments'

    id = sql.Column(sql.Integer, autoincrement=True, primary_key=True)

    comment_top = sql.Column(sql.String, nullable=True)
    comment_bottom = sql.Column(sql.String, nullable=True)
    rating = sql.Column(sql.Integer, nullable=False)
    post_date = sql.Column(sql.DateTime, default=datetime.datetime)
    creator = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    user = orm.relation('User')

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.comment_top, self.comment_bottom, self.rating, self.id, self.post_date)
