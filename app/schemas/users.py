from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    email: str = Field(
        title="Correo electrónico",
        description="Correo electrónico del usuario",
    )
    active: bool


class CreateUser(BaseUser):
    pass


class User(BaseModel):
    id: int
    email: str = Field(
        title="Correo electrónico",
        description="Correo electrónico del usuario",
    )
