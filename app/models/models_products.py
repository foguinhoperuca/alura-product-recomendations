from typing import List

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    category: str
    tags: List[str]


class CreateProduct(ProductBase):
    pass


class Product(ProductBase):
    id: int


class PurchaseHistory(BaseModel):
    products_ids: List[int]


class Preferences(BaseModel):
    categories: List[str] | None = None
    tags: List[str] | None = None
