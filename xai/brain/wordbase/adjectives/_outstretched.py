

#calss header
class _OUTSTRETCHED():
	def __init__(self,): 
		self.name = "OUTSTRETCHED"
		self.definitions = [u'reaching out as far as possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
