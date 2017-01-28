

#calss header
class _PROFLIGATE():
	def __init__(self,): 
		self.name = "PROFLIGATE"
		self.definitions = [u'spending money in a way that wastes it and is not wise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
