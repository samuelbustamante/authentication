# authentication
Módulo de Django 1.8 (python3) para autenticar por XML-RPC usuarios de la UNSL

Agragar en **settings.py** de proyecto:

```python
AUTHENTICATION_BACKENDS = (
    'authentication.backends.LoginBackend',
    )
```
