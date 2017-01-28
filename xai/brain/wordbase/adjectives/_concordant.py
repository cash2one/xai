

#calss header
class _CONCORDANT():
	def __init__(self,): 
		self.name = "CONCORDANT"
		self.definitions = [u'in agreement with other facts or based on the same principles as something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
