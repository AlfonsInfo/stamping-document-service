import base64
from PyPDF2 import PdfWriter, PdfReader, PaperSize, Transformation, PageObject
from PyPDF2.generic import RectangleObject, NameObject, NumberObject
import pdfkit
import qrcode

from PIL import Image
from io import BytesIO

import html_engine


def do_stamp(data, signature_base64, output_image_path):

    """
    :param file_input_base64: Base64 encoded input PDF file
    :param signature_base64: Base64 encoded signature image
    :param output_image_path: Path to save the temporary image of the stamp
    :return: Base64 encoded output PDF file
    """
    try:
        # Decode the input file
        file_bytes = base64.b64decode(data.fileBase64)
        file_input = BytesIO(file_bytes)

        # Open the PDF file from binary data
        existing_pdf = PdfReader(file_input, strict=False)
        box = existing_pdf.pages[0].mediabox

        # Decode the signature image
        signature_bytes = base64.b64decode(signature_base64)
        tempImage = Image.open(BytesIO(signature_bytes))
        if existing_pdf.pages[0].get('/Rotate') == 90:
            is_landscape = True
            h = box.getWidth()
            w = box.getHeight() * 3 / 4
            sign = tempImage.rotate(90, expand=1)
        else:
            is_landscape = False
            h = box.getWidth()
            w = box.getHeight() * 3 / 4
            sign = tempImage

        buff = BytesIO()
        sign.save(buff, format="PNG")
        base64s = base64.b64encode(buff.getvalue()).decode("utf-8")

        htmls = html_engine.generate_html(w, base64s, data, is_landscape)

        path_wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
        pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_string(htmls, output_image_path)

        stamp = PdfReader(open(output_image_path, "rb"))

        outputs = PdfWriter()
        # Merge pages
        count = existing_pdf.numPages
        for i in range(count):
            page = existing_pdf.pages[i]
            if i == 0:
                if existing_pdf.pages[0].get('/Rotate') == 90:
                    # Stamp for landscape
                    h = float(page.mediabox.height)
                    w = float(page.mediabox.width)
                    s = stamp.pages[0]

                    transform = Transformation().scale(0.9, 0.9).translate(300, 0)
                    s.add_transformation(transform)

                    s.cropbox = RectangleObject((0, 0, s.mediabox.height, s.mediabox.width))
                    page_A4 = PageObject.create_blank_page(width=w, height=h)
                    s.mediabox = page_A4.mediabox
                    page_A4.merge_page(s)

                    page.merge_page(page_A4)
                    outputs.add_page(page)
                else:
                    # Stamp for portrait
                    page.merge_page(stamp.pages[0])
                    outputs.add_page(page)
            else:
                outputs.add_page(page)

        output_buffer = BytesIO()
        outputs.write(output_buffer)
        output_buffer.seek(0)
        output_base64 = base64.b64encode(output_buffer.getvalue()).decode('utf-8')

        return output_base64

    except Exception as e:
        print(f"An error occurred: {e}")
        raise