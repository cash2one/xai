

#calss header
class _PEDANTIC():
	def __init__(self,): 
		self.name = "PEDANTIC"
		self.definitions = [u'giving too much attention to formal rules or small details: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
