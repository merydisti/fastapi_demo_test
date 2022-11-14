import ormar

from app.db import BaseMeta


class Sample(ormar.Model):
    class Meta(BaseMeta):
        tablename = "sample"

    name: str = ormar.String(primary_key=True,max_length=128, unique=True, nullable=False)
    description: str = ormar.String(max_length=128, unique=True, nullable=False)
