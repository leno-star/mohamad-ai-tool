from flask import Blueprint, request, jsonify
from backend.models.patterns import get_pattern_prompt
from backend.utils.ai_engine import generate_script_response

regenerate_bp = Blueprint('regenerate', __name__)

@regenerate_bp.route('/regenerate-script', methods=['POST'])
def regenerate_script():
    data = request.get_json()

    product = data.get('product')
    pattern = data.get('pattern')

    if not product or not pattern:
        return jsonify({'error': 'يرجى إدخال اسم المنتج والنمط المطلوب'}), 400

    # توليد صيغة جديدة بنفس النمط
    prompt = get_pattern_prompt(product, pattern)
    new_result = generate_script_response(prompt)

    return jsonify({'new_script': new_result})