from flask import Blueprint, request, jsonify
from backend.models.patterns import get_pattern_prompt
from backend.utils.ai_engine import generate_script_response

generate_bp = Blueprint('generate', __name__)

@generate_bp.route('/generate-script', methods=['POST'])
def generate_script():
    data = request.get_json()

    product = data.get('product')
    pattern = data.get('pattern')

    if not product or not pattern:
        return jsonify({'error': 'الرجاء إدخال اسم المنتج والنمط المطلوب'}), 400

    # جلب التوجيه المناسب للنمط
    prompt = get_pattern_prompt(product, pattern)

    # توليد السكربت من وحدة الذكاء
    result = generate_script_response(prompt)

    return jsonify({'script': result})