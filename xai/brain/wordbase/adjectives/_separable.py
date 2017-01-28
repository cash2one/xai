

#calss header
class _SEPARABLE():
	def __init__(self,): 
		self.name = "SEPARABLE"
		self.definitions = [u'able to be separated from each other']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
