# anndi

Experimental dependency injection that uses annotations.

## Install

```bash
pip install anndi
```


## Usage

Use `anndi.provides` for marking functions that provides some dependencies,
and use `anndi.injector` context manager for resolving dependencies:


```python
from anndi import provides, injector


@provides
def get_db_connection(*, settings: Settings) -> Connection:
    ...


@provides
def get_settings() -> Settings:
    ...
    
    
@provides
def get_cache(*, settings: Settings, db: Connection) -> CacheManager:
    ...


def init_app(*, settings: Settings, db: Connection, cache: CacheManager):
    ...
    
    
with injector() as resolver:
    resolver.run(init_app)

```


## License MIT
