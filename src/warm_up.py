import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest="command")

greet_parser = subparsers.add_parser("greet" , help="greet command")
greet_parser.add_argument("name" , type=str,help="name of the person to greet")

args =parser.parse_args()
if args.command =="greet":
    print(f"Hello {args.name}!")