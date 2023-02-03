#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import datetime
import argparse
import sys
sys.path.append("..")
import trace_source


parser = argparse.ArgumentParser()
parser.add_argument('--station', help='station name like limassol, barbados or mcmurdo')
#parser.add_argument('--date', help='date in the format YYYYMMDD')
#parser.add_argument('--daterange', help='date range in the format YYYYMMDD-YYYMMDD')

args = parser.parse_args()


#if args.station is not None and args.station != 'limassol':
if args.station is not None:
	config = 'config_{}.toml'.format(args.station)
else:
	config = 'config_ps113.toml'


tr_input = trace_source.simulations.gen_input(config_file=config)
tr_input.input_hysplit()
