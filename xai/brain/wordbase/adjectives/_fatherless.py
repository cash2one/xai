

#calss header
class _FATHERLESS():
	def __init__(self,): 
		self.name = "FATHERLESS"
		self.definitions = [u'without a father: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
