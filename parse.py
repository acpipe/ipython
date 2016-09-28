#
import argparse

parse = argparse.ArgumentParser()
parse.add_argument("echo", help="echo the string u use here ", type=int)

parse.add_argument("--version", help="this param print version of the script")
args = parse.parse_args()
if args.version:
    print
    "version : 0.0.1"
print
var = args.echo * 2
