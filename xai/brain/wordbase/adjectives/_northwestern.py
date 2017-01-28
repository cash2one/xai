

#calss header
class _NORTHWESTERN():
	def __init__(self,): 
		self.name = "NORTHWESTERN"
		self.definitions = [u'in or from the northwest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
