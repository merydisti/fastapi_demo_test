from pydantic import BaseModel, Field, validator
from decimal import Decimal


class CreateProduct(BaseModel):
    name: str = Field(
        title="Nombre",
        description="Nombre del producto",
    )
    active: bool
    price: float = Field(
        title="Precio",
        description="Precio en soles del producto",
    )
    price_dolars: Decimal = Field(
        title="Precio en dolares",
        description="Precio en dolares del producto",
    )
    active: bool

    @validator("price")
    def user_must_exist(cls, value):
        if value < 0:
            raise ValueError("El precio debe ser mayor a 0")
        return value


class Product(CreateProduct):
    id: int
