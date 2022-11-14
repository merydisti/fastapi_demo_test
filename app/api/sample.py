from fastapi import APIRouter, status

from app.models.sample import Sample
import app.schemas as schemas

router = APIRouter()


@router.get(
    "/", summary="Obtain", description=""
)
async def read_users():
    return await Sample.objects.all()


@router.post("/", summary="Create", status_code=status.HTTP_201_CREATED)
async def create_user(sample: schemas.CreateSample):
    return await Sample.objects.create(**sample.dict())


@router.get("/simplified", response_model=list[schemas.Sample])
async def read_users_simplified() -> list[schemas.Sample]:
    return await Sample.objects.all()
