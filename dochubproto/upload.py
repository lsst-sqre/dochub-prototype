"""Upload client for LSST the Docs.

This code should eventually go back to LTD Mason.
"""

import requests


class KeeperClient(object):
    """Build loader client for LTD Keeper.
    """

    def __init__(self, product_name, git_refs,
                 keeper_url, keeper_user, keeper_password):
        super().__init__()
        self.product_name = product_name
        self.git_refs = git_refs
        if isinstance(git_refs, str):
            self.git_refs = [self._git_refs]
        else:
            self.git_refs = git_refs
        self.keeper_url = keeper_url
        self.keeper_user = keeper_user
        self.keeper_password = keeper_password
        self.build_info = None  # Should be created by __enter__

    def __enter__(self):
        """Enter the context.

        The client uses this to declare a new build to the Keeper API.
        """
        keeper_token = self._authenticate()

        post_data = {'git_refs': self.git_refs}

        r = requests.post(
            self.keeper_url + '/products/{p}/builds/'.format(
                p=self.product_name),
            auth=(keeper_token, ''),
            json=post_data)
        if r.status_code != 201:
            raise RuntimeError(r.json())

        self.build_info = r.json()

    def __exit__(self, *args):
        """Exit the context.

        The client uses this to mark the build as uploaded in the Keeper API.
        """
        keeper_token = self._authenticate()
        r = requests.patch(self.build_info['self_url'],
                           auth=(keeper_token, ''),
                           json={'uploaded': True})
        self.log.debug(r.json())
        if r.status_code != 200:
            raise RuntimeError(r)

    def _authenticate(self):
        """Authenticate with LTD Keeper to get an API token."""
        token_endpoint = self.keeper_url + '/token'
        r = requests.get(token_endpoint,
                         auth=(self.keeper_user, self.keeper_password))
        self.log.debug(r.json())
        if r.status_code != 200:
            message = 'Could not authenticate to {0}: error {1:d}\n{2}'
            self.log.error(message)
            raise RuntimeError(message.format(token_endpoint,
                                              r.status_code,
                                              r.json()))
        return r.json()['token']

    @property
    def surrogate_key(self):
        """Fastly surrogate key to apply for uploaded build objects."""
        self.build_info['surrogate_key']

    @property
    def s3_prefix(self):
        """Path prefix for the build."""
        self.build_info['bucket_root_dir']
