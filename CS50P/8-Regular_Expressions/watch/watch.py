import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
  # Expresión regular para encontrar una URL de YouTube en el atributo src del iframe
    pattern = r'src="(https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+))"'
    match = re.search(pattern, s)

    if match:
        # Extraer el identificador del video de YouTube (el segundo grupo)
        video_id = match.group(2)
        # Retornar la URL corta de YouTube
        return f"https://youtu.be/{video_id}"
    return None


if __name__ == "__main__":
    main()
