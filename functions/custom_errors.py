# Objects:
# # EmptyListError
# # ItemNotFoundError
# # NodeNotFoundError
# # MethodNotFoundError


class EmptyListError(KeyError):
    pass


class ItemNotFoundError(KeyError):
    pass


class NodeNotFoundError(KeyError):
    pass


class MethodNotFoundError(KeyError):
    pass
