keyboard_0 = ["abcdefghijklm",\
            "nopqrstuvwxyz"]
keyboard_1 = ["789",    \
            "456",  \
            "123",  \
            "0.-"]
keyboard_2 = ["chunk",  \
            "vibex",    \
            "gymps",    \
            "fjord",    \
            "waltz"]
keyboard_3 = ["bemix",  \
            "vozhd",    \
            "grypt",    \
            "clunk",    \
            "waqfs"]
keyboard = [keyboard_0,keyboard_1,keyboard_2,keyboard_3]
for line in keyboard_0:
    print(line)
    if "n" in line:
        print(str(keyboard_0.index(line)) + str(line.index("n")))