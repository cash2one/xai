

#calss header
class _VETERAN():
	def __init__(self,): 
		self.name = "VETERAN"
		self.definitions = [u'having been involved in a particular activity for a long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
