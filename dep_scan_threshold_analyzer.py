import sys

from depscan.analyzer.thresholdanalyzer import ThresholdAnalyzer

# get file report location from environment variable
report_file_src = sys.argv[1]
cvss_score_threshold = float(sys.argv[2])

analyzer = ThresholdAnalyzer(report_file_src, cvss_score_threshold)

if analyzer.run() is True:
    sys.exit(1)
