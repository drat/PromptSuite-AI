import json
import os

# --- Cek variabel lingkungan untuk templates ---
template_json = os.getenv('PROMPT_TEMPLATES', '{}')

try:
    # Parsing data JSON dengan penanganan error
    data_prompt = json.loads(template_json)
except json.JSONDecodeError:
    # Jika JSON tidak valid, fallback ke dict kosong
    data_prompt = {}

# --- Daftar metaprompt Fallback (10 yang Deddy minta) ---
daftar_metaprompt_fallback = [
    "comprehensive_multistage",
    "structured_roleplaying",
    "balanced_scientific",
    "quick_simplified",
    "logical_flow",
    "flexible_technique",
    "autoregressive_reasoning",
    "mathematical_proof",
    "sequential_contextual",
    "attention_aware"
]

# --- Deskripsi fallback untuk tiap metaprompt ---
penjelasan_metaprompt_fallback = {
    "comprehensive_multistage": "Pendekatan multi-tahap yang komprehensif dan bertingkat.",
    "structured_roleplaying": "Simulasi peran dengan struktur yang jelas.",
    "balanced_scientific": "Keseimbangan antara sains, logika, dan objektivitas.",
    "quick_simplified": "Hasil cepat dan penyederhanaan dalam eksekusi.",
    "logical_flow": "Alur berpikir yang logis dan runtut.",
    "flexible_technique": "Teknik adaptif, fleksibel untuk berbagai kasus.",
    "autoregressive_reasoning": "Penalaran progresif, tahap demi tahap.",
    "mathematical_proof": "Pendekatan matematis dan pembuktian formal.",
    "sequential_contextual": "Proses bertahap dan mempertimbangkan konteks.",
    "attention_aware": "Memaksimalkan fokus dan perhatian pada poin penting."
}

# --- Prioritaskan dari JSON ENV jika ada, jika tidak fallback ke default di atas ---
if data_prompt:
    daftar_metaprompt = [kunci for kunci in data_prompt.keys()]
    penjelasan_metaprompt = {
        kunci: data.get("description", "Tidak ada deskripsi")
        for kunci, data in data_prompt.items()
    }
else:
    daftar_metaprompt = daftar_metaprompt_fallback
    penjelasan_metaprompt = penjelasan_metaprompt_fallback

print("Daftar Metaprompt:", daftar_metaprompt)

# --- Markdown penjelasan untuk UI ---
penjelasan_markdown = "".join([
    f"- **{kunci}**: {isi}\n"
    for kunci, isi in penjelasan_metaprompt.items()
])

# --- Daftar model yang tersedia ---
daftar_model = [
    "meta-llama/Meta-Llama-3-70B-Instruct",
    "meta-llama/Meta-Llama-3-8B-Instruct",
    "meta-llama/Llama-3.1-70B-Instruct",
    "meta-llama/Llama-3.1-8B-Instruct",
    "meta-llama/Llama-3.2-3B-Instruct",
    "meta-llama/Llama-3.2-1B-Instruct",
    "meta-llama/Llama-2-13b-chat-hf",
    "meta-llama/Llama-2-7b-chat-hf",
    "HuggingFaceH4/zephyr-7b-beta",
    "HuggingFaceH4/zephyr-7b-alpha",
    "Qwen/Qwen2.5-72B-Instruct",
    "Qwen/Qwen2.5-1.5B",
    "microsoft/Phi-3.5-mini-instruct"
]

# --- Mengambil contoh prompt dari JSON templates (jika ada) ---
contoh_prompt = []
for kunci, data in data_prompt.items():
    contoh_template = data.get("examples", [])
    if contoh_template:
        contoh_prompt.extend([
            [contoh[0], kunci] if isinstance(contoh, list) else [contoh, kunci]
            for contoh in contoh_template
        ])

# --- Token API ---
api_token = os.getenv('HF_API_TOKEN')
if not api_token:
    raise ValueError("HF_API_TOKEN tidak ditemukan di environment variable")

# --- Dictionary meta_prompts (template prompt) ---
meta_prompts = {
    kunci: data.get("template", "Template tidak tersedia")
    for kunci, data in data_prompt.items()
} if data_prompt else {k: "" for k in daftar_metaprompt}

# --- Model default untuk refiner, dari env atau fallback ---
model_refiner_prompt = os.getenv('prompt_refiner_model', 'meta-llama/Llama-3.1-8B-Instruct')
print("Model refiner prompt yang digunakan:", model_refiner_prompt)

# --- Variabel tambahan dari environment jika ada ---
echo_refiner_prompt = os.getenv('echo_prompt_refiner')
openai_metaprompt = os.getenv('openai_metaprompt')
metaprompt_lanjut = os.getenv('advanced_meta_prompt')

# --- Ekspor alias variabel supaya tetap kompatibel dengan app.py ---
metaprompt_list = daftar_metaprompt
explanation_markdown = penjelasan_markdown
models = daftar_model

examples = [
    ["Buatlah ringkasan mendalam mengenai dampak revolusi industri 4.0 terhadap pola kerja masyarakat urban di Indonesia, dengan menyoroti perubahan sosial, ekonomi, serta tantangan sumber daya manusia di era digital.", "comprehensive_multistage"],
    ["Bertindaklah sebagai pakar komunikasi publik dan simulasi tanya jawab antara seorang menteri dan wartawan terkait isu kenaikan harga bahan pokok, lengkap dengan dialog dan argumentasi masing-masing pihak.", "structured_roleplaying"],
    ["Analisis secara kritis data pertumbuhan ekonomi Indonesia dalam lima tahun terakhir, dan jelaskan faktor-faktor utama yang mempengaruhi fluktuasi angka tersebut secara ilmiah dan objektif.", "balanced_scientific"],
    ["Sederhanakan penjelasan tentang blockchain sehingga mudah dipahami oleh pelajar SMA, namun tetap mencakup mekanisme dasar, manfaat, serta potensi risikonya.", "quick_simplified"],
    ["Jelaskan urutan logis proses produksi energi listrik dari sumber energi terbarukan, mulai dari tahap input sumber daya, konversi energi, distribusi, hingga konsumsi akhir oleh masyarakat.", "logical_flow"]
]
metaprompt_explanations = penjelasan_metaprompt

