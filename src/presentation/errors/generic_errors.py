class GenericClientError(Exception):
    def __init__(self, error: str, detailed_error: str = None):
        super().__init__(error, detailed_error)


class GenericServerError(Exception):
    def __init__(self, error: str, detailed_error: str = None):
        super().__init__(error, detailed_error)
