class Config(object):
    
    TESTING = False
    
    SECRET_KEY = '35646GHGTFDEHT/%&/($%(&%&/$%&/VFDGFH))'
    
    
class Developmentconfig(Config):
    
    DEBUG = True
    
    
class ProductionConfig(Config):
    
    DEBUG = False
    
    
class TestingConfig(Config):
    
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    