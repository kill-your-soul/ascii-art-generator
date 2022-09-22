from PIL import Image


def get_str_ascii(intent: int) -> str:
    index = int(intent / 32)
    ascii = [" ", ".", ",", "-", "~", "+", "=", "@"]
    return ascii[index]


def get_ascii_art(path: str, scale: int) -> None:
    img = Image.open(path)
    width, height = img.size
    for y in range(0, height):
        for x in range(0, width):
            if y % (scale * 2) == 0 and x % scale == 0:
                pix = img.getpixel((x, y))
                intent = pix[0] / 3 + pix[1] / 3 + pix[2] / 3
                try:
                    if pix[3] == 0:
                        intent = 0
                except IndexError:
                    pass
                print(get_str_ascii(intent), end="")
        if y % (scale * 2) == 0:
            print()


def main():
    print("Hello to terminal ASCII art generator")
    input_image = input("Input path to image to convert to ascii art: ")
    scale = int(input("Input scale: "))
    get_ascii_art(input_image, scale)


if __name__ == "__main__":
    main()
