class Registry(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def set(self, wrapped):
        self.wrapped = wrapped

    def __getattr__(self, k):
        return getattr(self.wrapped, k)
