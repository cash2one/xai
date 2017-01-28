

#calss header
class _SPONGY():
	def __init__(self,): 
		self.name = "SPONGY"
		self.definitions = [u'soft and able to absorb or having already absorbed a lot of liquid, like a sponge']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
