

#calss header
class _ARCANE():
	def __init__(self,): 
		self.name = "ARCANE"
		self.definitions = [u'mysterious and known only by a few people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
