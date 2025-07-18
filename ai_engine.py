import random

def generate_script_response(prompt: str) -> str:
    # هون ممكن تركّب توليد حقيقي باستخدام OpenAI أو نموذج محلي لاحقًا
    # بس مبدئيًا، نستخدم توليد وهمي تجريبي لتجربة الواجهة

    responses = [
        f"{prompt} 👀 هل أنت مستعد لاكتشاف القوة؟",
        f"{prompt} 💥 المنتج يلي عم تبحث عنه صار بين إيديك.",
        f"{prompt} ✨ الوقت المثالي لتجربة التميّز بدأ الآن.",
        f"{prompt} 🔥 خلّي حماسك يشتغل… وعيش التجربة.",
        f"{prompt} 💎 الجودة ما بتنقال… بتنشاف بهذا المنتج!"
    ]

    return random.choice(responses)