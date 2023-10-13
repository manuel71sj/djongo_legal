from djongo_legal.exceptions import NotSupportedError, print_warn

print_warn('validation')

class CollectionSchema:

    def __init__(self):
        raise NotSupportedError('Collection Schema')
