from fpdf import FPDF
import pandas as pd

pdf =FPDF(orientation="P",unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
#getting the topics from file
df= pd.read_csv("topics.csv")
line_spacing=10
no_of_pages=0

for index,row in df.iterrows():

    for i in range(row["Pages"]):

        no_of_pages = no_of_pages + 1

        #adding pages
        pdf.add_page()
        #Cell1 set the font for each cell
        pdf.set_font( family="Times",size=24,style="B")
        pdf.set_text_color(100,100,100) #whitecolor is 250:250:250
        pdf.cell(w=0,h=12,txt = row["Topic"],align="L",ln=1)

        for yaxis in range(20,278,line_spacing):
            pdf.line(10, yaxis, 200, yaxis)

        #set the footer with page numbers
        pdf.ln(260)
        pdf.set_font(family="Times", size=10, style="I")
        pdf.set_text_color(180, 180, 180)  # whitecolor is 250:250:250
        pdf.cell(w=0, h=12, txt=f"Pages {no_of_pages}", align="R")

pdf.output(("Output.pdf"))
print(f"{no_of_pages} Pages created Successfully")

