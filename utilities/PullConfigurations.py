from configparser import ConfigParser
def read_configurations(category,keyword):
    config = ConfigParser()
    config.read('configurations/config.ini')
    return config.get(category,keyword)
