from app.validators.product_validator import validate_product

def run_product_validation(product):

    issues = validate_product(product)

    quality_score = 100

    for issue in issues:

        if issue["severity"] == "HIGH":
            quality_score -= 30

        elif issue["severity"] == "MEDIUM":
            quality_score -= 15

        else:
            quality_score -= 5

    quality_score = max(0, quality_score)

    return {
        "issues": issues,
        "quality_score": quality_score
    }