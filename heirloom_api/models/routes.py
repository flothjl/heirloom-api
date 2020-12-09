class BaseRoute:
    '''
    Base helper class for defining routes
    '''
    def __init__(self, rule, view_func, options):
        self.rule = rule
        self.view_func = view_func
        self.options = options
