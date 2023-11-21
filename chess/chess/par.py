import argparse
import sys

class Parser:
    def __init__(self) -> None:
        self.parser=argparse.ArgumentParser()
        self.action_group=self.parser.add_mutually_exclusive_group(required=True)
        self.action_group.add_argument(
            '--add-player',
            dest='action',
            action='store_const',
            const='add_player',
            help='Dodawanie zawodnika zawodów'
        )
        self.action_group.add_argument(
            '--add-round',
            dest='action',
            action='store_const',
            const='add_round',
            help='Dodawanie rundy'
        )
        self.action_group.add_argument(
            '--shuffle',
            dest='action',
            action='store_const',
            const='shuffle',
            help='losujemy zawodników'
        )
        self.add_group = self.parser.add_argument_group('Add Arguments')
        self.add_group.add_argument(
            '--name',
            type=str,
            required='--add-player' in sys.argv
        )
        self.add_group.add_argument(
            '--surname',
            type=str,
            required='--add-player' in sys.argv
        )
    def parse_args(self):
        return self.parser.parse_args()   