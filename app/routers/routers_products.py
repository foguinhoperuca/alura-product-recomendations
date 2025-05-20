from typing import Dict, List

from fastapi import APIRouter, HTTPException

from app.models.models_product import Product, CreateProduct, PurchaseHistory, Preferences
from .routes_users import users


router: APIRouter = APIRouter()
products: List[Product] = []
product_counter: int = 1
purchase_history: Dict[int, List[int]] = {}


@router.post('/products/', response_model=Product)
def create_product(product: CreateProduct) -> Product:
    """
    Create a new product.
    Args:
        product: CreateProduct = The object that contains product's data.
    Returns:
        product: Product = The object with an id.
    """
    global product_counter
    new_product = Product(id=product_counter, **product.model_dump())
    products.append(new_product)
    product_counter += 1

    return new_product


@router.get('/products/', response_model=List[Product])
def list_products() -> List[Product]:
    """
    List all products registered.
    Returns:
        List[Product]: An list of all objects (products) registered.
    """
    return products


@router.post('/purchase_history/{user_id}')
def add_purchase_order(user_id: int, purchases: PurchaseHistory) -> Dict[str, str]:
    """
    Added or update th user's purchase history.
    Args:
        user_id: int = The id of user that will have the purchase order updated.
        purchases: PurchaseHistopry = The object with ids of purchased products.
    Returns:
        message: Dict[str, str] = A message telling that the purchase history has been updated.
    """
    if user_id not in [user.id for user in users]:
        raise HTTPException(status_code=404, detail='User not found!!')

    purchase_history[user_id] = purchases.product_ids

    return {'message': 'Purchase history updated!!'}


@router.post('/recommendations/{user_id}', response_model=List[Product])
def recommend_product(user_id: int, preferences: Preferences) -> List[Product]:
    """
    TODO document it!!
    """
    if user_id not in purchase_history:
        raise HTTPException(status_code=404, detail='Purchase history not found!!')

    recommend_products: List = [p for p_id in purchase_history[p_id] for p in products if p.id == p_id]
    recommend_product_categories: List = [p for p in recommended_products if p.category in preferences.category]
    filtered_recommend_products: List = []
    for product in recommend_product_categories:
        for tag in product.tag:
            if tag in preferences.tags:
                filtered_recommend_products.append(product)
                break

    return filtered_recommend_products
