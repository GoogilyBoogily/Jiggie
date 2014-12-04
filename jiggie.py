import os, sys, logging, argparse, json

from helper import config

parser = argparse.ArgumentParser(description='Jiggie')
parser.add_argument('--debug', action='store_true', help='Show debug messages')
args = parser.parse_args()


if __name__ == '__main__':
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print(" Jiggie Voice Commands ")
    print(" Made By: Derek Mayer")
    print("~~~~~~~~~~~~~~~~~~~~~~")

    logging.basicConfig()
    logger = logging.getLogger()

