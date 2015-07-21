import argparse

argparser = argparse.ArgumentParser(description='help string goes here')

argparser.add_argument('--flag1')

args = argparser.parse_args()

print args.flag1
