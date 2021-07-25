import argparse

def spoiler(text):
    return "".join([f"||{a}||" for a in text])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Spoil a text')
    parser.add_argument('text', type=str, nargs='*',
                        help='Text to be turned into a spoiler')
    args = parser.parse_args()
    if len(args.text) < 1:
        spoil = input("Type a word to make it spoiler: ")
        print("There you go, copy and paste it to Discord:")
    else:
        spoil = ""
        for i in range(len(args.text)):
            if i == len(args.text) - 1:
                spoil += args.text[i]
            else:
                spoil += args.text[i] + " "
    print(spoiler(spoil))
