from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class Entity(BaseModel, Generic[T]):
    """The entity model with unique identifier."""

    model_config = ConfigDict(extra="forbid")

    entity_id: T = Field(..., description="Entity ID.")


class ValueObject(BaseModel):
    """A marker model for immutable value objects."""

    model_config = ConfigDict(extra="forbid", frozen=True)
