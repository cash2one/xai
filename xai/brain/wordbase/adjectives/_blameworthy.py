

#calss header
class _BLAMEWORTHY():
	def __init__(self,): 
		self.name = "BLAMEWORTHY"
		self.definitions = [u'having done something wrong']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
