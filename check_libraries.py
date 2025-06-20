import importlib

libraries = [
    ('pandas', 'pd'),
    ('numpy', 'np'),
    ('sklearn', 'sklearn'),
    ('xgboost', 'xgb'),
    ('shap', 'shap'),
    ('scipy', 'scipy'),
    ('matplotlib', 'plt')
]

for lib_name, alias in libraries:
    try:
        module = importlib.import_module(lib_name)
        version = getattr(module, '__version__', 'version attribute not found')
        print(f"{lib_name} is installed, version: {version}")
    except ImportError:
        print(f"{lib_name} is NOT installed.")
