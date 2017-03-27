"""dochub-prototype renders the DocHub prototype website and publishes it to
LSST the Docs.
"""

import argparse

from .dochubproto import DocHubProto


def parse_args():
    parser = argparse.ArgumentParser(
        description='Render the DocHub prototype website and publish it to '
                    'LSST the Docs.')
    parser.add_argument(
        '--keeper-user', dest='keeper_user', required=True,
        help='Keeper username')
    parser.add_argument(
        '--keeper-password', dest='keeper_password', required=True,
        help='Keeper password')
    parser.add_argument(
        '--aws-id', dest='aws_id', required=True,
        help='AWS key ID')
    parser.add_argument(
        '--aws-secret', dest='aws_secret', required=True,
        help='AWS secret key')
    parser.add_argument(
        '--ref', default='master',
        help='Git ref (like `master`) that becomes the edition name. Use '
             '`master` for the main edition, but other git refs can be '
             'given for staging. Default is `master`.')
    return parser.parse_args()


def main():
    args = parse_args()

    renderer = DocHubProto()
    renderer.upload_site(
        keeper_user=args.keeper_user,
        keeper_password=args.keeper_password,
        aws_access_key_id=args.aws_id,
        aws_secret_access_key=args.aws_secret,
        git_refs=args.ref)
