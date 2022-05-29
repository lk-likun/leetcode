from reportlab.pdfgen import canvas


def hello(c):
    c.drawString(1, 100, "Hello World")


c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()
