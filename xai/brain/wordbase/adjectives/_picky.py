

#calss header
class _PICKY():
	def __init__(self,): 
		self.name = "PICKY"
		self.definitions = [u'Someone who is picky is very careful about choosing only what they like: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
