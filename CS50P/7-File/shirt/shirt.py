import csv,sys,os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input.JPEG/PNG output.JPEG/PNG")

    input = sys.argv[1]
    output = sys.argv[2]
    valid_extensions = (".jpg", ".jpeg", ".png")

    if not input.lower().endswith(valid_extensions):
        sys.exit("Error: The input file must have a .jpg, .jpeg, or .png extension")

    if not output.lower().endswith(valid_extensions):
        sys.exit("Error: The output file must have a .jpg, .jpeg, or .png extension")

    # Verificar que las extensiones del archivo de entrada y salida coincidan
    if os.path.splitext(input)[1].lower() != os.path.splitext(output)[1].lower():
        sys.exit("Error: Input and output files must have the same extension")

    if not os.path.isfile(input):
        sys.exit(f"Error: File '{input}' does not exist ")

    try:
        input = Image.open(input)

        shirt = Image.open("shirt.png")

        input = ImageOps.fit(input,shirt.size)

        input.paste(shirt,shirt)

        input.save(output)

    except Exception as e:
        sys.exit(f"Error: Could not read the file. {e}")


if __name__ == "__main__":
    main()
