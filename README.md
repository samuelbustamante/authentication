# authentication
Módulo de Django para autenticar por XML-RPC usuarios de la UNSL

Agragar en **settings.py** de proyecto:

```python
AUTHENTICATION_BACKENDS = (
    'authentication.backends.LoginBackend',
    )
```
