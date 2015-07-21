import argparse

argparser = argparse.ArgumentParser(description='blah')

argparser.add_argument('position_args', nargs='+')

argparser.add_argument('--targetsfile')

args = argparser.parse_args()

print args.position_args
print args.targetsfile
