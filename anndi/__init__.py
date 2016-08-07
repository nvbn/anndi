from contextlib import contextmanager
from weakref import WeakValueDictionary

_provides = WeakValueDictionary()


class Injector:
    """Resolve and inject dependencies."""

    def __init__(self):
        self._resolved = {}

    def _get_value(self, name):
        """Get dependency by name (type)."""
        if name not in _provides:
            raise ValueError("Dependency {} not registered.".format(
                name))

        if name not in self._resolved:
            fn = _provides[name]
            kwargs = self._get_dependencies(fn)
            return fn(**kwargs)
        return self._resolved[name]

    def _get_dependencies(self, fn):
        """Get dependencies for function."""
        return {key: self._get_value(value)
                for key, value in fn.__annotations__.items()
                if key != 'return'}

    def run(self, fn):
        """Resolve dependencies and run function."""
        kwargs = self._get_dependencies(fn)
        return fn(**kwargs)


@contextmanager
def injector():
    yield Injector()


def provides(fn):
    """Register function that provides something."""

    try:
        _provides[fn.__annotations__['return']] = fn
    except KeyError:
        raise ValueError('Function not annotated.')

    return fn
