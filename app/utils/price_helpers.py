def calculate_price_difference(
    our_price,
    competitor_price
):

    difference = our_price - competitor_price

    percentage = (
        difference / competitor_price
    ) * 100

    return {
        "difference": round(difference, 2),
        "percentage_difference": round(percentage, 2)
    }