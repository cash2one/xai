

#calss header
class _PACIFIC():
	def __init__(self,): 
		self.name = "PACIFIC"
		self.definitions = [u'peaceful or helping to cause peace']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
