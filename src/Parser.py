from Decoder import Decoder
from Timestamp import Timestamp
import re
import sys 
import binascii

class Parser:
    def __init__(self, dbc):
        self.format = None
        self.plot = Decoder(dbc)
        self.timestamp = Timestamp()
        self.define_mask()
        self.parse_dump()

    def define_mask(self):
        # Matches 'candump' output, i.e. "vcan0  1F0   [8]  00 00 00 00 00 00 1B C1".
        self.RE_CANDUMP = re.compile(r'^\s*(?:\((?P<time>.*?)\))?\s*\S+\s+(?P<frameid>[0-9A-F]+)\s*\[\d+\]\s*(?P<data>[0-9A-F ]*)(?:\s*::.*)?$')
        # Matches 'cantools decode' output, i.e. ")" or "   voltage: 0 V,".
        self.RE_DECODE = re.compile(r'\w+\(|\s+\w+:\s+[0-9.+-]+(\s+.*)?,?|\)')
        # Matches 'candump -l' (or -L) output, i.e. "(1594172461.968006) vcan0 1F0#0000000000001BC1"
        self.RE_CANDUMP_LOG = re.compile(r'^\((?P<time>\d+\.\d+)\)\s+\S+\s+(?P<frameid>[\dA-F]+)#(?P<data>[\dA-F]*)$')
        self.mask_list = (self.RE_CANDUMP, self.RE_DECODE, self.RE_CANDUMP_LOG)

    def find_mask(self, line):
        if not self.format:
            for mask in self.mask_list:
                match = mask.match(line)
                if match:
                    self.format = mask 
                    return match
        else:
            return self.format.match(line)

    def match_unpack(self, match):
        # extract the data from a re match object
        timestamp = float(match.group('time'))
        frame_id = int(match.group('frameid'), 16)
        data = binascii.unhexlify(match.group('data').replace(' ',''))
        return timestamp, frame_id, data

    def parse_dump(self):
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            line = line.strip('\r\n')
            if not line:
                continue
            match = self.find_mask(line)
            raw_timestamp, frame_id, data = self.match_unpack(match)
            timestamp = self.timestamp.duration(raw_timestamp)
            self.plot.add_msg(timestamp, frame_id, data)
        self.plot.plot()
