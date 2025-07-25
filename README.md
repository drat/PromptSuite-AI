# 🚀 PromptSuite AI

![banner-propmptsuite](https://github.com/user-attachments/assets/02ad2ba4-06c7-40a9-a12f-b5287b8e8df9)

PromptSuite AI adalah platform rekayasa prompt canggih untuk **menganalisis, membandingkan, dan memperbaiki prompt** berbasis Large Language Model (LLM).
Didesain khusus untuk peneliti, praktisi AI, developer, hingga pemula yang ingin mengeksplorasi *prompt engineering* dan efek optimasinya terhadap kualitas output AI.

---

## ✨ Fitur Utama

* 🔮 **Otomatisasi Perbaikan Prompt:** Pilih otomatis metode/metaprompt terbaik berdasarkan input Anda.
* 🛠️ **Perbaikan Manual & Custom:** Pilih dari berbagai *metaprompt* dan eksplor gaya optimasi berbeda.
* 🧠 **Support Multi-Model:** Bisa membandingkan hasil pada banyak model open source LLM.
* 📊 **Tab Perbandingan Output:** Lihat side-by-side output prompt asli & hasil refine dengan jelas.
* 📋 **Contoh Prompt Panjang:** Sudah tersedia puluhan contoh prompt bahasa Indonesia siap pakai.
* 🧾 **Output JSON Lengkap:** Lihat full response model untuk riset & debugging.
* 🎨 **UI Modern, Responsif, & Custom Theme:** Dengan dukungan CSS premium & dark theme merah, serta emoji di seluruh UI!
* 🔒 **Siap untuk Cloud maupun Lokal:** Dirancang modular & production-ready.

---

## 🖼️ Screenshot

<img width="1785" height="2033" alt="Gradio-07-25-2025_08_36_PM" src="https://github.com/user-attachments/assets/7baf63b5-e2fc-46f8-b344-1a75ed6a3f8d" />

---

## 🚀 Demo Singkat

1. Masukkan prompt Anda di kolom utama, atau pilih dari *Contoh Prompt*.
2. Klik **🔮 Pilih Otomatis Metode Perbaikan** untuk saran otomatis, atau pilih metaprompt manual.
3. Klik **✨ Perbaiki Prompt** untuk melihat hasil & penjelasan perbaikan.
4. Pilih model yang ingin diuji, lalu klik **⚡ Uji Prompt ke Model**.
5. Bandingkan output asli & refine di tab-tab yang tersedia, atau cek output mentah di panel JSON.

---

## ⚙️ Instalasi & Jalankan Lokal

### 1. Clone repository

```bash
git clone https://github.com/username/PromptSuiteAI.git
cd PromptSuiteAI
```

### 2. Buat environment (opsional, disarankan)

```bash
python -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

**(Pastikan menggunakan Gradio versi 4.x terbaru!)**

### 4. Jalankan aplikasi

```bash
python app.py
```

Akses di browser via [http://localhost:7860](http://localhost:7860)

---

## 🔧 Struktur Folder

```
PromptSuiteAI/
├─ app.py
├─ variables.py
├─ prompt_refiner.py
├─ custom_css.py
├─ themes.py
├─ requirements.txt
├─ README.md
└─ (file & asset pendukung lain)
```

---

## 🔥 Contoh Prompt Panjang (Bahasa Indonesia)

* Buatlah ringkasan mendalam mengenai dampak revolusi industri 4.0 terhadap pola kerja masyarakat urban di Indonesia, dengan menyoroti perubahan sosial, ekonomi, serta tantangan sumber daya manusia di era digital.
* Bertindaklah sebagai pakar komunikasi publik dan simulasi tanya jawab antara seorang menteri dan wartawan terkait isu kenaikan harga bahan pokok, lengkap dengan dialog dan argumentasi masing-masing pihak.
* Analisis secara kritis data pertumbuhan ekonomi Indonesia dalam lima tahun terakhir, dan jelaskan faktor-faktor utama yang mempengaruhi fluktuasi angka tersebut secara ilmiah dan objektif.
* Sederhanakan penjelasan tentang blockchain sehingga mudah dipahami oleh pelajar SMA, namun tetap mencakup mekanisme dasar, manfaat, serta potensi risikonya.
* Jelaskan urutan logis proses produksi energi listrik dari sumber energi terbarukan, mulai dari tahap input sumber daya, konversi energi, distribusi, hingga konsumsi akhir oleh masyarakat.

---

## 🧩 Arsitektur Modular

```
Gradio UI 4.x + Theme
        │
        ▼
 [PromptSuiteAI Controller]
        │
        ├─ PromptRefiner (PemurniPrompt)
        ├─ Variables & Templates (Metaprompt)
        └─ Output: Multi-model, Tab, JSON, dsb.
```

---

## 💬 Kontribusi

* Pull Request, feedback, atau usulan metaprompt baru sangat terbuka!
* Ingin kolaborasi AI riset/edukasi di Indonesia? DM via [LinkedIn](https://linkedin.com/in/dratnanto) atau \[email di profile].

---

## © 2025 \_\_drat

> Siapa yang menguasai prompt, dialah yang mengendalikan hasil AI! 🚀
