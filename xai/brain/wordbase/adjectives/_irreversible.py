

#calss header
class _IRREVERSIBLE():
	def __init__(self,): 
		self.name = "IRREVERSIBLE"
		self.definitions = [u'not possible to change; impossible to return to a previous condition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
