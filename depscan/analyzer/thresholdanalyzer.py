import json
import logging

from log.logger import log


class ThresholdAnalyzer:
    src: str
    threshold: float
    logger: logging.Logger

    def __init__(self, src: str, threshold: float):
        self.src = src
        self.threshold = threshold
        self.logger = log

    def run(self) -> bool:
        try:
            with open(self.src, "r") as file:
                data = json.load(file)

                for vuln in data["vulnerabilities"]:
                    for rating in vuln["ratings"]:

                        cvss_score = float(rating["score"])
                        if cvss_score >= self.threshold:
                            self.logger.error(
                                f"One or more dependencies were identified with vulnerabilities that have a CVSS score greater than or equal to '{self.threshold}'")
                            return True
        except FileNotFoundError:
            self.logger.warning("There are no report files in the reports folder")

        self.logger.info("This report file doesn't contains any dependencies with vulnerabilities")
