def product_schema(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product.get("description"),
        "price": product["price"],
        "stock": product.get("stock", 0),
        "images": product.get("images", []),
        "main_image": product.get("main_image"),
        "active": product.get("active", True),
        "created_by": product.get("created_by"),
        "updated_by": product.get("updated_by"),
        "created_at": product.get("created_at"),
        "updated_at": product.get("updated_at"),
    }


def products_schema(products):
    return [product_schema(p) for p in products]