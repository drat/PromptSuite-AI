"""
PromptSuite AI
==============

Deskripsi Proyek:
-----------------
PromptSuite AI adalah platform rekayasa prompt modern untuk membandingkan, menganalisis,
dan memperbaiki prompt secara otomatis ataupun manual, berbasis Large Language Model (LLM) open source.
Platform ini dirancang untuk peneliti, praktisi AI, developer, dan siapapun yang ingin mengeksplorasi
efek optimasi prompt terhadap kualitas output AI.

Fitur:
------
- Perbandingan output prompt original & hasil refine (multi-tab, side-by-side)
- Refinement otomatis maupun manual, dengan berbagai metaprompt canggih
- UI responsif dengan status tombol dinamis & reset otomatis
- Panel JSON untuk output full response (debug/research)
- Dukungan custom CSS & styling profesional
- Bisa dijalankan di lokal, server, maupun cloud

Teknologi:
----------
- Gradio advanced + custom JS + modular backend PromptRefiner
- Fleksibel untuk model apapun (tinggal sesuaikan backend PromptRefiner)
- Siap untuk pengembangan riset atau industri

"""

import gradio as gr
from prompt_refiner import PemurniPrompt
from variables import api_token, models, meta_prompts, explanation_markdown, metaprompt_list, metaprompt_explanations, examples
from custom_css import custom_css
from themes import IndonesiaTheme

class PromptSuiteAI:
    def __init__(self, prompt_refiner: PemurniPrompt, custom_css):
        self.prompt_refiner = prompt_refiner
        default_model = models[-1] if len(models) >= 1 else models[0] if models else None

        with gr.Blocks(theme=IndonesiaTheme(), css=custom_css) as self.interface:
            # --- HEADER & TITLE ---
            with gr.Column(elem_classes=["container", "title-container"]):
                gr.HTML("""
                  <div style='text-align: center;'>
                        <img src='https://i.ibb.co.com/ynqKvrr/banner-pulid.jpg' alt='Banner' style='width: 100%; max-width:820px; height: auto; border-radius:16px; box-shadow:0 2px 12px 0 rgba(30,30,30,0.12); margin-bottom:0.7em;'/>
                    </div>
                """)
                gr.Markdown("# 🚀 PromptSuite AI")
                gr.Markdown("### 🤖 Otomatisasi dan Perbandingan Rekayasa Prompt LLM")
                gr.Markdown("🔍 Bandingkan, evaluasi, dan optimasi prompt AI Anda secara praktis dan canggih.")
                gr.Markdown(
                    """
                    <span style='font-size:1.03em; color:#ccc'>
                    ✨ <b>PromptSuite AI</b> adalah platform rekayasa prompt modern untuk membandingkan, menganalisis, 
                    dan memperbaiki prompt secara otomatis ataupun manual, berbasis Large Language Model (LLM) open source.<br>
                    💡 Platform ini dirancang untuk peneliti, praktisi AI, developer, dan siapapun yang ingin mengeksplorasi 
                    efek optimasi prompt terhadap kualitas output AI.
                    </span>
                    """,
                    unsafe_allow_html=True
                )

            # --- KONTENER 2: Input Prompt & Contoh ---
            with gr.Column(elem_classes=["container", "input-container"]):
                prompt_text = gr.Textbox(label="✏️ Tulis prompt Anda (atau kosongkan untuk melihat metaprompt)", lines=5)
                with gr.Accordion("📋 Contoh Prompt", open=False, visible=True):     
                    gr.Examples(examples=examples, inputs=[prompt_text]) 
                automatic_metaprompt_button = gr.Button(
                    "🔮 Pilih Otomatis Metode Perbaikan",
                    elem_classes=["button-highlight"]
                )
                MetaPrompt_analysis = gr.Markdown()

            # --- KONTENER 3: Pilihan Metaprompt & Penjelasan ---
            with gr.Column(elem_classes=["container", "meta-container"]):
                meta_prompt_choice = gr.Radio(
                    choices=metaprompt_list,
                    label="🛠️ Pilih Metaprompt",
                    value=metaprompt_list[0],
                    elem_classes=["no-background", "radio-group"]
                )
                refine_button = gr.Button(
                    "✨ Perbaiki Prompt",
                    elem_classes=["button-waiting"]
                )
                with gr.Accordion("ℹ️ Penjelasan Metaprompt", open=False, visible=True): 
                    gr.Markdown(explanation_markdown)

            # --- KONTENER 4: Analisis & Refined Prompt ---
            with gr.Column(elem_classes=["container", "analysis-container"]):           
                gr.Markdown(" ")
                prompt_evaluation = gr.Markdown()
                gr.Markdown("### ✨ Prompt yang Telah Diperbaiki")
                refined_prompt = gr.Textbox(
                    label=" ",
                    interactive=True,
                    show_label=True,
                    show_copy_button=True,
                )
                explanation_of_refinements = gr.Markdown()

            # --- KONTENER 5: Pilihan Model & Output Tab ---
            with gr.Column(elem_classes=["container", "model-container"]):
                with gr.Row():
                    apply_model = gr.Dropdown(
                        choices=models,
                        value=default_model,
                        label="🧠 Pilih Model",
                        container=False,
                        scale=1,
                        min_width=300
                    )
                    apply_button = gr.Button(
                        "⚡ Uji Prompt ke Model",
                        elem_classes=["button-waiting"]
                    )
                gr.Markdown("### 📝 Hasil Pada Model Terpilih")
                with gr.Tabs(elem_classes=["tabs"]):
                    with gr.TabItem("📊 Perbandingan Output", elem_classes=["tabitem"]):                     
                        with gr.Row(elem_classes=["output-row"]):
                            with gr.Column(scale=1, elem_classes=["comparison-column"]):
                                gr.Markdown("### 🔡 Output Prompt Asli")
                                original_output1 = gr.Markdown(
                                    elem_classes=["output-content"],
                                    visible=True
                                )
                            with gr.Column(scale=1, elem_classes=["comparison-column"]):
                                gr.Markdown("### ✨ Output Prompt Diperbaiki")
                                refined_output1 = gr.Markdown(
                                    elem_classes=["output-content"],
                                    visible=True
                                )
                    with gr.TabItem("🔡 Output Prompt Asli", elem_classes=["tabitem"]):
                        with gr.Row(elem_classes=["output-row"]):
                            with gr.Column(scale=1, elem_classes=["comparison-column"]):
                                gr.Markdown("### 🔡 Output Prompt Asli")
                                original_output = gr.Markdown(
                                    elem_classes=["output-content"],
                                    visible=True
                                )
                    with gr.TabItem("✨ Output Prompt Diperbaiki", elem_classes=["tabitem"]):
                        with gr.Row(elem_classes=["output-row"]):
                            with gr.Column(scale=1, elem_classes=["comparison-column"]):
                                gr.Markdown("### ✨ Output Prompt Diperbaiki")
                                refined_output = gr.Markdown(
                                    elem_classes=["output-content"],
                                    visible=True
                                )
                with gr.Accordion("🧾 Respons JSON Lengkap", open=False, visible=True):
                    full_response_json = gr.JSON()

            # ======================= EVENT HANDLER / JS ==========================

            def automatic_metaprompt(prompt: str):
                if not prompt.strip():
                    return "Silakan masukkan prompt untuk dianalisis.", None
                metaprompt_analysis, recommended_key = self.prompt_refiner.automatic_metaprompt(prompt)
                return metaprompt_analysis, recommended_key

            def refine_prompt(prompt: str, meta_prompt_choice: str):
                if not prompt.strip():
                    return ("Tidak ada prompt.", "", "", {})
                result = self.prompt_refiner.refine_prompt(prompt, meta_prompt_choice)
                return (
                    result[0],  # Evaluasi awal prompt
                    result[1],  # Prompt diperbaiki
                    result[2],  # Penjelasan perbaikan
                    result[3]   # Full JSON response
                )

            def apply_prompts(original_prompt: str, refined_prompt_: str, model: str):
                if not original_prompt or not refined_prompt_:
                    return (
                        "Silakan isi prompt asli dan hasil refine.",
                        "Silakan isi prompt asli dan hasil refine.",
                        "Silakan isi prompt asli dan hasil refine.",
                        "Silakan isi prompt asli dan hasil refine."
                    )
                if not model:
                    return (
                        "Pilih model terlebih dahulu.",
                        "Pilih model terlebih dahulu.",
                        "Pilih model terlebih dahulu.",
                        "Pilih model terlebih dahulu."
                    )
                try:
                    original_output = self.prompt_refiner.apply_prompt(original_prompt, model)
                    refined_output_ = self.prompt_refiner.apply_prompt(refined_prompt_, model)
                except Exception as e:
                    err = f"Terjadi error: {str(e)}"
                    return (err, err, err, err)
                return (
                    str(original_output) if original_output else "Tidak ada output.",
                    str(refined_output_) if refined_output_ else "Tidak ada output.",
                    str(original_output) if original_output else "Tidak ada output.",
                    str(refined_output_) if refined_output_ else "Tidak ada output."
                )

            # --- Event click dan chain JS custom, sama persis dengan kode asli ---
            automatic_metaprompt_button.click(
                fn=automatic_metaprompt,
                inputs=[prompt_text],
                outputs=[MetaPrompt_analysis, meta_prompt_choice]
            ).then(
                fn=lambda: None,
                inputs=None,
                outputs=None,
                js="""
                    () => {
                        document.querySelectorAll('.analysis-container textarea, .analysis-container .markdown-text, .model-container .markdown-text, .comparison-output').forEach(el => {
                            if (el.value !== undefined) {
                                el.value = '';
                            } else {
                                el.textContent = '';
                            }
                        });
                        const allButtons = Array.from(document.querySelectorAll('button')).filter(btn => 
                            btn.textContent.includes('Pilih Otomatis') || 
                            btn.textContent.includes('Perbaiki Prompt') || 
                            btn.textContent.includes('Uji Prompt')
                        );
                        allButtons.forEach(btn => btn.classList.remove('button-highlight'));
                        allButtons[1].classList.add('button-highlight');
                        allButtons[0].classList.add('button-completed');
                        allButtons[2].classList.add('button-waiting');
                    }
                """
            )

            refine_button.click(
                fn=refine_prompt,
                inputs=[prompt_text, meta_prompt_choice],
                outputs=[prompt_evaluation, refined_prompt, explanation_of_refinements, full_response_json]
            ).then(
                fn=lambda: None,
                inputs=None,
                outputs=None,
                js="""
                    () => {
                        document.querySelectorAll('.model-container .markdown-text, .comparison-output').forEach(el => {
                            if (el.value !== undefined) {
                                el.value = '';
                            } else {
                                el.textContent = '';
                            }
                        });
                        const allButtons = Array.from(document.querySelectorAll('button')).filter(btn => 
                            btn.textContent.includes('Pilih Otomatis') || 
                            btn.textContent.includes('Perbaiki Prompt') || 
                            btn.textContent.includes('Uji Prompt')
                        );
                        allButtons.forEach(btn => btn.classList.remove('button-highlight'));
                        allButtons[2].classList.add('button-highlight');
                        allButtons[1].classList.add('button-completed');
                        allButtons[2].classList.remove('button-waiting');
                    }
                """
            )

            apply_button.click(
                fn=apply_prompts,
                inputs=[prompt_text, refined_prompt, apply_model],
                outputs=[original_output, refined_output, original_output1, refined_output1],
                show_progress=True
            ).then(
                fn=lambda: None,
                inputs=None,
                outputs=None,
                js="""
                    () => {
                        const allButtons = Array.from(document.querySelectorAll('button')).filter(btn => 
                            btn.textContent.includes('Pilih Otomatis') || 
                            btn.textContent.includes('Perbaiki Prompt') || 
                            btn.textContent.includes('Uji Prompt')
                        );
                        allButtons.forEach(btn => btn.classList.remove('button-highlight', 'button-waiting'));
                        allButtons[2].classList.add('button-completed');
                        document.querySelectorAll('.comparison-output').forEach(el => {
                            if (el.parentElement) {
                                el.parentElement.style.display = 'none';
                                setTimeout(() => {
                                    el.parentElement.style.display = 'block';
                                }, 100);
                            }
                        });
                    }
                """
            )

            prompt_text.change(
                fn=lambda: None,
                inputs=None,
                outputs=None,
                js="""
                    () => {
                        document.querySelectorAll('.analysis-container textarea, .analysis-container .markdown-text, .model-container .markdown-text, .comparison-output').forEach(el => {
                            if (el.value !== undefined) {
                                el.value = '';
                            } else {
                                el.textContent = '';
                            }
                        });
                        const allButtons = Array.from(document.querySelectorAll('button')).filter(btn => 
                            btn.textContent.includes('Pilih Otomatis') || 
                            btn.textContent.includes('Perbaiki Prompt') || 
                            btn.textContent.includes('Uji Prompt')
                        );
                        allButtons.forEach(btn => {
                            btn.classList.remove('button-completed', 'button-highlight', 'button-waiting');
                        });
                        allButtons[0].classList.add('button-highlight');
                        allButtons.slice(1).forEach(btn => btn.classList.add('button-waiting'));
                    }
                """
            )

    def launch(self, share=False):
        """Jalankan antarmuka PromptSuite AI"""
        self.interface.launch(share=share)

if __name__ == '__main__':
    prompt_refiner = PemurniPrompt(api_token, meta_prompts, metaprompt_explanations)
    app = PromptSuiteAI(prompt_refiner, custom_css)
    app.launch(share=False)
