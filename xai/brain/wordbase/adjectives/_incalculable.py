

#calss header
class _INCALCULABLE():
	def __init__(self,): 
		self.name = "INCALCULABLE"
		self.definitions = [u'extremely large and therefore unable to be measured: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
