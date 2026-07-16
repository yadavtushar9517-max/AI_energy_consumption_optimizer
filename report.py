from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generate_pdf(data, filename="Energy_Report.pdf"):

    pdf = SimpleDocTemplate(filename)

    table_data = [list(data.columns)] + data.values.tolist()

    table = Table(table_data)

    table.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.grey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('GRID',(0,0),(-1,-1),1,colors.black),
        ('BACKGROUND',(0,1),(-1,-1),colors.beige),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('BOTTOMPADDING',(0,0),(-1,0),12),
    ]))

    pdf.build([table])

    return filename