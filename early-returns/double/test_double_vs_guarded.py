from double import double
from guarded_double import guarded_double

assert guarded_double(None) is double(None) is None
assert guarded_double(1) == double(1) == 2
