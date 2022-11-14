from app.schemas.sample_schema import SampleSchema


def before_insert_sample(name="Sample 1", description="Sample description 1"):
    sample = SampleSchema(
        name=name,
        description=description
    )
    SampleSchema.objects.create(**sample.dict())

