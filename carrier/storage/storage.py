
import pg
import redis

class Storage:
    def __init__(self):
        print 'Storage init'
        self.db = pg.PGRepository()
        self.cache = redis.RedisRepository()

    def saveCarrier(carrier):
        print 'saving carrier'
