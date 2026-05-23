def validate_product(product):

    issues = []

    if not product.title:

        issues.append({
            "severity": "HIGH",
            "message": "Missing title",
            "suggested_fix": "Add a product title"
        })

    elif len(product.title) < 10:

        issues.append({
            "severity": "MEDIUM",
            "message": "Very short title",
            "suggested_fix": "Add more descriptive keywords"
        })

    if product.price <= 0:

        issues.append({
            "severity": "HIGH",
            "message": "Invalid price",
            "suggested_fix": "Price should be positive"
        })

    if product.mrp and product.mrp < product.price:

        issues.append({
            "severity": "HIGH",
            "message": "MRP lower than selling price",
            "suggested_fix": "Correct MRP or selling price"
        })

    if not product.brand:

        issues.append({
            "severity": "MEDIUM",
            "message": "Missing brand",
            "suggested_fix": "Add product brand"
        })

    return issues