from pocha import after_each, it


@after_each
def setup():
    raise Exception('doing it on purpose')

@it('can run a passing it')
def _():
    pass

@it('can run another passing it')
def _():
    pass
