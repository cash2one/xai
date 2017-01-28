

#calss header
class _INHABITABLE():
	def __init__(self,): 
		self.name = "INHABITABLE"
		self.definitions = [u'able to be lived in or on']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
