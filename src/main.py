import argparse
from Parser import Parser
import os 

def main():
    parser = argparse.ArgumentParser(description='Decoding package from candump flow.\
                                     The package will get the stdout of the pipe command candump.\
                                     The data from CAN messages will be decoded and stored.')
    parser.add_argument('--channel', help='CAN channel configuration. Example: dbc1, dbc2, dbc3, dbc4.')
    args = parser.parse_args()
    dbc = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dbc', args.channel + '.dbc')
    Parser(dbc)

if __name__=="__main__":
    main()
