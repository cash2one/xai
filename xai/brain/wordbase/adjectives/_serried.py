

#calss header
class _SERRIED():
	def __init__(self,): 
		self.name = "SERRIED"
		self.definitions = [u'pressed closely together, usually in lines: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
