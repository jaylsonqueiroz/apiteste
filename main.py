from flask import Flask, request
import pdfkit

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_html_to_pdf():
    html = request.data.decode('utf-8')
    pdf_path = 'exemplo.pdf'
    options = {
        'page-size': 'Letter',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm'
    }
    pdfkit.from_string(html, pdf_path, options=options)
    return f'PDF gerado em: {pdf_path}'

if __name__ == '__main__':
    app.run(debug=True)
