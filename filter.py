#import cb58ref
#import bech32
import sys

if __name__ == "__main__":
    block = None
    with open(sys.argv[1], "r") as f:
        for line in f:
            lp = [t.strip() for t in line.split(',')]
            if len(lp) != 8:
                continue
            if len(lp[1]) == 0:
                block = lp[-1]
                continue
            if len(lp[1]) < 2:
                continue
            #b = cb58ref.cb58decode(lp[1])
            #lp[1] = "P-" + bech32.bech32_encode('avax', bech32.convertbits(b, 8, 5, True))
            print(",".join(lp[:-2] + [str(block)]))
