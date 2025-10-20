from flask import Flask, request, send_file
import barcode
from barcode.writer import ImageWriter
from io import BytesIO

app = Flask(__name__)

@app.route('/barcode')
def generate_barcode():
    text = request.args.get('data', '')
    if not text:
        return "Parámetro 'data' requerido", 400

    try:
        code128 = barcode.get('code128', text, writer=ImageWriter())
        buffer = BytesIO()
        code128.write(buffer, {'module_height': 10.0, 'font_size': 10})
        buffer.seek(0)
        return send_file(buffer, mimetype='image/png')
    except Exception as e:
        return f"Error generando código de barras: {str(e)}", 500
