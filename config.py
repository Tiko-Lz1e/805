# config.py
import config_default
import pandas

configs = config_default.configs

try:
    import config_override
    configs['Token'] = config_override.configs['Token']
except ImportError:
    pass
