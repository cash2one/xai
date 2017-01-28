

#calss header
class _SEASONAL():
	def __init__(self,): 
		self.name = "SEASONAL"
		self.definitions = [u'relating to or happening during a particular period in the year: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
