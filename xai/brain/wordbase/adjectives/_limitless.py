

#calss header
class _LIMITLESS():
	def __init__(self,): 
		self.name = "LIMITLESS"
		self.definitions = [u'without limit: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
