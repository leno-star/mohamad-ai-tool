def get_pattern_prompt(product: str, pattern: str) -> str:
    if pattern == "teaser":
        return f"اكتب سكربت تشويقي لمنتج اسمه '{product}'، يثير الفضول ويجذب الانتباه."

    elif pattern == "story":
        return f"اكتب سكربت قصصي يحكي قصة مستخدم اشترى '{product}' وكيف تغيرت حياته."

    elif pattern == "speedy":
        return f"اكتب سكربت سريع ومباشر يشرح فوائد '{product}' خلال ثوانٍ."

    elif pattern == "luxury":
        return f"اكتب سكربت تسويقي بلغة فاخرة وأنيقة تبرز مستوى '{product}' العالي."

    else:
        return f"اكتب نص تسويقي مميز لمنتج اسمه '{product}'."