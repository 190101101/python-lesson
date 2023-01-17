p1 = ("Peter", "Parker", 28)

p2 = "Hi %s %s. Aren't you %d years old?"
print(p2 % p1)


#

file = {
	"path": "./com/pyt",
	"version": 1.8,
	"author": "apsi"
}

data = "%(version)1.f version file with '%(path)s' address is written as %(author)s" % file
print(data)