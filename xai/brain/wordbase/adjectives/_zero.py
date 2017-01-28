

#calss header
class _ZERO():
	def __init__(self,): 
		self.name = "ZERO"
		self.definitions = [u'not any or no: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
