def generate_enhanced_title(product):

    brand = product.brand or ""
    color = product.color or ""
    category = product.category or ""
    material = product.material or ""

    enhanced_title = f"{brand} {color} {category} with {material}"

    enhanced_title = enhanced_title.strip()

    return {
        "original_title": product.title,
        "enhanced_title": enhanced_title,
        "keywords": [
            category,
            color,
            material
        ]
    }