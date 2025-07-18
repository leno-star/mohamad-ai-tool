from flask import Blueprint, request, jsonify
import datetime

feedback_bp = Blueprint('feedback', __name__)
feedback_storage = []  # تخزين مؤقت داخل الذاكرة (ممكن نركّب تخزين دائم لاحقًا)

@feedback_bp.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()

    message = data.get('message')
    user = data.get('user', 'مستخدم مجهول')

    if not message:
        return jsonify({'error': 'يرجى كتابة الملاحظة'}), 400

    feedback_entry = {
        'user': user,
        'message': message,
        'timestamp': datetime.datetime.now().isoformat()
    }

    feedback_storage.append(feedback_entry)

    return jsonify({'status': 'تم استلام الملاحظة بنجاح 🙌'})