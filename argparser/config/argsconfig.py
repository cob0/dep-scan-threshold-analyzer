import argparse
from argparse import ArgumentParser, Namespace

ARGS_DESCRIPTION = ("A binary tool that verifies if vulnerability reports generated by dep-scan comply with predefined "
                    "security thresholds. It outputs OK if the vulnerabilities are within the threshold or FAIL if they "
                    "exceed the allowed values.")


class Arguments:
    instance: Namespace | None = None

    def __init__(self) -> None:
        if Arguments.instance is None:
            self.instance = self._init_args()

    def _init_parser(self) -> ArgumentParser:
        return argparse.ArgumentParser(description=ARGS_DESCRIPTION)

    def _init_args(self) -> Namespace:
        parser = self._init_parser()
        parser.add_argument("-f", "--file", type=str,
                            help="specifies the directory where the reports are stored. This argument is required and "
                                 "must point to the folder containing the relevant reports.",
                            required=True)
        parser.add_argument("-t", "--threshold", type=float,
                            help="defines the threshold level used to determine when a vulnerability or issue should "
                                 "be considered a failure. This argument is required and it sets the sensitivity for "
                                 "identifying critical problems.",
                            required=True)
        return parser.parse_args()


args = Arguments().instance
