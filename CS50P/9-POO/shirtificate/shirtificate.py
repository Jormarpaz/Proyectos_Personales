from fpdf import FPDF

def main():
    name = input("What's your name? ")
    create_shirtificate(name)

def create_shirtificate(name):
    # Create PDF object with portrait orientation and A4 format
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # Set the font for the title
    pdf.set_font("Arial", "B", 24)
    pdf.set_text_color(0, 0, 0)  # Black color for the text

    # Add the title "CS50 Shirtificate" centered at the top of the page
    pdf.cell(0, 40, "CS50 Shirtificate", ln=True, align='C')

    # Add the image of the shirt (centered horizontally)
    shirt_x = (pdf.w - 210) / 2  # Center the image horizontally
    shirt_y = 60
    shirt_width = 210
    pdf.image("shirtificate.png", x=shirt_x, y=shirt_y, w=shirt_width)

    # Set the font for the name
    pdf.set_font("Arial", "B", 32)
    pdf.set_text_color(255, 255, 255)  # White color for the text

    # Calculate the position for the name
    name_y = shirt_y + 40  # Adjust this value based on the image size and desired position

    # Move to the calculated position and add the user's name, centered
    pdf.set_y(name_y)
    pdf.cell(0, 10, f"{name}", ln=True, align='C')

    # Output the PDF to a file called shirtificate.pdf
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
