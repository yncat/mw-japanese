import sys
import translator


def run():
    if len(sys.argv) != 2:
        print("Usage: Give the filename to parse.")
        return 0
        # end usage

    f = open(sys.argv[1], "r", encoding="UTF-8")
    c = f.readlines()
    f.close()
    original_lines = range(0, len(c), 3)
    target_lines = range(1, len(c), 3)
    for o, t in zip(original_lines, target_lines):
        c[t] = translator.translate(c[o])
    # end translate
    f = open(sys.argv[1], "w", encoding="UTF-8")
    f.writelines(c)
    # end write
    f.close()


sys.exit(run())
