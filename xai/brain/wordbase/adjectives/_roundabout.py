

#calss header
class _ROUNDABOUT():
	def __init__(self,): 
		self.name = "ROUNDABOUT"
		self.definitions = [u'not in a simple, direct, or quick way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
