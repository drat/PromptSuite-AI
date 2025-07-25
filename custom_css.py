# File ini awalnya digunakan untuk menyimpan custom CSS untuk tampilan Gradio.
# Namun, sesuai instruksi, aplikasi sekarang tidak menggunakan CSS custom sama sekali.
# Tidak perlu mengisi kode apapun di file ini.

custom_css = """
#col-left, #col-mid {
    margin: 0 auto;
    max-width: 400px;
    padding: 10px;
    border-radius: 15px;
    background-color: #f9f9f9;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
#col-right {
    margin: 0 auto;
    max-width: 400px;
    padding: 10px;
    border-radius: 15px;
    background: linear-gradient(180deg, #B6BBC4, #EEEEEE);
    color: white;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
#col-bott {
    margin: 0 auto;
    padding: 10px;
    border-radius: 15px;
    background-color: #f9f9f9;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
#banner {
    width: 100%;
    text-align: center;
    margin-bottom: 20px;
}
#run-button {
    background-color: #ff4b5c;
    color: white;
    font-weight: bold;
    padding: 30px;
    border-radius: 10px;
    cursor: pointer;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
#footer {
    text-align: center;
    margin-top: 20px;
    color: silver;
}
#markdown-silver {
    color: silver; /* Mengatur warna font Markdown menjadi silver */
}
"""
