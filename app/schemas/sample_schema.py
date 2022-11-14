from pydantic import BaseModel, Field


class SampleSchema(BaseModel):
    name: str = Field(
        title="Sample title",
        description="Sample description",
    )
    description: str = Field(
        title="Sample title",
        description="Sample description",
    )


