

#calss header
class _DIACRITICAL():
	def __init__(self,): 
		self.name = "DIACRITICAL"
		self.definitions = [u'written above or below a letter to change its pronunciation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
