from app.models.sample import Sample


async def before_insert_sample(name="Sample 1", description="Sample description 1"):
    sample = Sample(
        name=name,
        description=description
    )
    await Sample.objects.create(**sample.dict())

