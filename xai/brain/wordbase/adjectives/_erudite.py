

#calss header
class _ERUDITE():
	def __init__(self,): 
		self.name = "ERUDITE"
		self.definitions = [u'having or containing a lot of knowledge that is known by very few people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
