import fpdf


def main():
    make_tshirt(input("Name: "))


def make_tshirt(name):
    pdf = fpdf.FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=0, y=0)
    pdf.set_font("helvetica", style="B", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 70)
    pdf.cell(0, 10, f"{name} took CS50", align='C')
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
