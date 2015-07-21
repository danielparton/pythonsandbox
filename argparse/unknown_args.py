import argparse

argparser = argparse.ArgumentParser(description='blah')

# argparser.add_argument('position_args', nargs='+')

argparser.add_argument('--targetsfile')

args, unknown = argparser.parse_known_args()

print args
print unknown
