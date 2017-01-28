

#calss header
class _KINDA():
	def __init__(self,): 
		self.name = "KINDA"
		self.definitions = [u'used in writing to represent an informal way of saying "kind of": ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
