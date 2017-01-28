

#calss header
class _VERDANT():
	def __init__(self,): 
		self.name = "VERDANT"
		self.definitions = [u'covered with healthy green plants or grass: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
