

#calss header
class _SHAMEFACED():
	def __init__(self,): 
		self.name = "SHAMEFACED"
		self.definitions = [u'awkward and embarrassed or ashamed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
