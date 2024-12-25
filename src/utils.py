import pathlib
import yaml

def read_config(config_path:pathlib.Path):
    """
    Read config file
    Parameters
    ----------
    config_path : pathlib.Path
        The path to the configuration file.

    Returns
    -------
    dict
        The configuration data loaded from the file.
    """
    with open(str(config_path), 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config


    