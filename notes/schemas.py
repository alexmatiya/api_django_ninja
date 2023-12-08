from ninja import Schema, ModelSchema, Field
from datetime import date
from .models import Note
from typing import Optional


class CategoryIn(Schema):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)


class CategoryOut(Schema):
    id: int
    title: str
    description: str


class NoteIn(ModelSchema):
    class Config:
        model = Note
        model_fields = ['title', 'category']


class NoteUpd(ModelSchema):
    class Config:
        model = Note
        model_fields = ['id', 'completed']


class NoteOut(ModelSchema):
    class Config:
        model = Note
        model_fields = ['id', 'title', 'category', 'created', 'completed']
