import sys

from log.logger import print_logo

print_logo()

from argparser.config.argsconfig import args
from depscan.analyzer.thresholdanalyzer import ThresholdAnalyzer

analyzer = ThresholdAnalyzer(args.file, args.threshold)

if analyzer.run() is True:
    sys.exit(1)
