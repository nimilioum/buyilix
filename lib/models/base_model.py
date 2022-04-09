import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


class TimestampMixin(object):
    created_at = sa.Column(sa.DateTime, server_default=func.now())
    updated_at = sa.Column(sa.DateTime, server_default=func.now(), onupdate=func.now())


class Base(declarative_base(), TimestampMixin):
    __abstract__ = True

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, index=True, unique=True)
