import ormar
from decimal import Decimal

from app.db import BaseMeta


class Product(ormar.Model):
    class Meta(BaseMeta):
        tablename = "products"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=128, nullable=False)
    price: float = ormar.Float(default=0.0, nullable=False)
    price_dolars: Decimal = ormar.Decimal(
        default=0.0, decimal_places=2, max_digits=10, nullable=False
    )
    active: bool = ormar.Boolean(default=True, nullable=False)
