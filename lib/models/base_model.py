import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone


class TimestampMixin(object):
    created_at = sa.Column(sa.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = sa.Column(sa.DateTime,default=lambda: datetime.now(timezone.utc))


class BaseModel(declarative_base(), TimestampMixin):
    __abstract__ = True

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
