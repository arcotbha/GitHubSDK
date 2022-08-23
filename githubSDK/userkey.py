from base import GitHubBase


class UserKey(GitHubBase):
    def __init__(self, requester, attributes):
        super().__init__(requester, attributes)
        self._id = attributes['id']
        self._key = attributes['key']

    def __repr__(self):
        return self.get__repr__({"id": self._id})

    @property
    def id(self):
        """
        :type: integer
        """
        return self._id

    @property
    def key(self):
        """
        :type: string
        """
        return self._key
