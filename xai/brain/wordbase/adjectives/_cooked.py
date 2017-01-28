

#calss header
class _COOKED():
	def __init__(self,): 
		self.name = "COOKED"
		self.definitions = [u'Cooked food has been prepared by heating: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
