from fpdf import FPDF
import pandas as pd

pdf =FPDF(orientation="P",unit="mm",format="A4")
df= pd.read_csv("topics.csv")

for index,row in df.iterrows():
    #adding pages
    pdf.add_page()
    #Cell1 set the font for each cell
    pdf.set_font( family="Times",size=24,style="B")
    pdf.set_text_color(100,100,100) #whitecolor is 250:250:250
    pdf.cell(w=0,h=12,txt = row["Topic"],align="L",ln=1)
    pdf.line(10,21,200,21)

pdf.output(("Output.pdf"))
print("PDF created Successfully")

