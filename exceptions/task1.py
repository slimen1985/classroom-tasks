import logging


def config_loggin(verb_level):
    if verb_level < 1:
        raise ValueError(f"level cannot be less than 1")
    logging.basicConfig(level=verb_level)


config_loggin(0)
