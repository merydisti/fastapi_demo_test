from pydantic import BaseModel, Field


class Sample(BaseModel):
    name: str = Field(
        title="Sample title",
        description="Sample description",
    )
    description: str = Field(
        title="Sample title",
        description="Sample description",
    )

class CreateSample(Sample):
    pass

