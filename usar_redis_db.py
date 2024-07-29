import redis

#para o nó master
cmaster = redis.StrictRedis(host="127.0.0.1", port=6379, db=0, password='abcd1234')

cmaster.set('diogo', 200)
print('O valor do diogo é', cmaster.get('diogo'))

# na résplica não consegue escrever, só consegue ler

cmaster = redis.StrictRedis(host="127.0.0.1", port=6380, db=0)

cmaster.set('diogo', 200)
print('O valor do diogo é', cmaster.get('diogo'))
