#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for word in sorted(dir(hidden_4)):
        if word[0:2] != '__':
            print("{}".format(word), end="\n")
