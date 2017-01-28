

#calss header
class _INDUSTRIOUS():
	def __init__(self,): 
		self.name = "INDUSTRIOUS"
		self.definitions = [u'An industrious person works hard: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
