from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.ln(10)
pdf.set_font("Times", style = "BIU", size=50)
pdf.set_text_color(220,20,60)
title = "CS50 Shirtificate"
pdf.set_x((pdf.w - pdf.get_string_width(title))/2)
pdf.cell(text = title)

pdf.ln(40)

image_width = (pdf.w - pdf.l_margin - pdf.r_margin)
pdf.set_x((pdf.w - image_width)/2)
pdf.image("shirtificate.png", w = image_width)

name = input("Enter your name: ")
pdf.set_font("Courier", style = "I", size = 30)
pdf.set_text_color(255,255,255)
pdf.set_xy(((pdf.w - pdf.get_string_width(title))/2), (pdf.get_y() - 140))
pdf.multi_cell(w = 100, text = f"{name} took CS50", align = "C")

pdf.output("shirtificate.pdf")
