import abc
from anndi import Injector, provides


class AbstractKeyValueStore(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set(self, key, value):
        ...

    @abc.abstractmethod
    def get(self, key, default=None):
        ...


class KeyValueStore(AbstractKeyValueStore):
    def __init__(self):
        self._store = {}

    def set(self, key, value):
        self._store[key] = value

    def get(self, key, default=None):
        return self._store.get(key, default)


@provides
def kv_store() -> AbstractKeyValueStore:
    store = KeyValueStore()
    store.set('init', True)
    return store


def app(store: AbstractKeyValueStore):
    store.set('app', True)
    assert store.get('init')
    return store.get('app')


def test():
    assert Injector().run(app)
