from fastapi import APIRouter, status

from app.models.users import User
import app.schemas as schemas

router = APIRouter()


@router.get(
    "/", summary="Obtener usuarios", description="Obtener a todos los usuarios de la BD"
)
async def read_users():
    return await User.objects.all()


@router.post("/", summary="Crear un nuevo usuario", status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.CreateUser):
    return await User.objects.create(**user.dict())


@router.get("/simplified", response_model=list[schemas.User])
async def read_users_simplified() -> list[schemas.User]:
    return await User.objects.all()
