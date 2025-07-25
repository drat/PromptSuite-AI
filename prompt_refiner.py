# Kelas PemurniPrompt digunakan untuk menganalisis dan memperbaiki prompt sesuai metode/metaprompt yang dipilih pengguna

class PemurniPrompt:
    def __init__(self, api_token, meta_prompts, metaprompt_explanations):
        self.api_token = api_token
        self.meta_prompts = meta_prompts
        self.metaprompt_explanations = metaprompt_explanations

    def automatic_metaprompt(self, prompt):
        """
        Otomatis memilih metaprompt terbaik berdasarkan isi prompt user.
        Return tuple: (analisis, saran_metaprompt)
        """
        # Algoritma dummy — bisa di-upgrade sesuai kebutuhan!
        if not prompt or prompt.strip() == "":
            return "Prompt kosong. Silakan isi prompt.", None

        # Heuristik sederhana: Jika panjang, pilih comprehensive_multistage, jika mengandung 'data', pilih balanced_scientific
        if "data" in prompt.lower():
            analisis = "Prompt ini berkaitan dengan data, disarankan 'balanced_scientific'."
            return analisis, "balanced_scientific"
        elif len(prompt.split()) > 25:
            analisis = "Prompt cukup kompleks, disarankan 'comprehensive_multistage'."
            return analisis, "comprehensive_multistage"
        else:
            analisis = "Prompt normal, gunakan 'logical_flow' untuk hasil optimal."
            return analisis, "logical_flow"

    def refine_prompt(self, prompt, metaprompt_key):
        """
        Melakukan perbaikan prompt secara manual dengan metaprompt terpilih.
        Return: (evaluasi, prompt_baru, penjelasan, full_response)
        """
        if not prompt or prompt.strip() == "":
            return ("Tidak ada prompt yang diberikan.", "", "", {})

        # Dummy refining — gabungkan template metaprompt dengan prompt user
        template = self.meta_prompts.get(metaprompt_key, "")
        if template:
            prompt_baru = f"{template.strip()}\n{prompt.strip()}"
        else:
            prompt_baru = f"[{metaprompt_key}]\n{prompt.strip()}"

        evaluasi = f"Prompt telah diperbaiki menggunakan metaprompt '{metaprompt_key}'."
        penjelasan = self.metaprompt_explanations.get(metaprompt_key, "Tidak ada penjelasan tersedia.")
        full_response = {
            "prompt_awal": prompt,
            "prompt_baru": prompt_baru,
            "metaprompt": metaprompt_key,
            "evaluasi": evaluasi,
            "penjelasan": penjelasan
        }
        return (evaluasi, prompt_baru, penjelasan, full_response)

    def apply_prompt(self, prompt, model):
        """
        Mensimulasikan pengujian prompt pada model LLM.
        Return: string output hasil 'jawaban model'
        """
        if not prompt or not model:
            return "Prompt atau model kosong."

        # Dummy output — ganti dengan pemanggilan API model Anda jika siap
        return f"(MODEL: {model})\nHASIL:\n{prompt[:400]} ...[Output simulasi LLM]"
