from flask import Blueprint, request, jsonify
from backend.models.patterns import get_pattern_prompt
from backend.utils.ai_engine import generate_script_response

vip_bp = Blueprint('vip_session', __name__)

@vip_bp.route('/vip-session', methods=['POST'])
def vip_session():
    data = request.get_json()

    product = data.get('product')
    secret_code = data.get('secret', '')

    # تحقق من الكود السري
    if secret_code != "VIP🔥":
        return jsonify({'error': 'رمز الدخول غير صحيح'}), 403

    # توليد سكربت فاخر خاص بالـ VIP
    prompt = f"اكتب سكربت فاخر جدًا لمنتج اسمه '{product}'، بأسلوب راقٍ ومميز لا يُستخدم في التوليد العادي."
    result = generate_script_response(prompt)

    return jsonify({'vip_script': result})