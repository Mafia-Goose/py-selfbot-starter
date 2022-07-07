import argparse


def start_parser():
    parser = argparse.ArgumentParser(description="Account script runner")
    parser.add_argument("-t", "--token", type=str, help="Token of account to run")
    parser.add_argument("-u", "--user", type=str, help="User to run", default="mayo")
    return parser
