

#calss header
class _AIRLESS():
	def __init__(self,): 
		self.name = "AIRLESS"
		self.definitions = [u'used to describe a place where it is difficult to breathe or the air is not fresh: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
