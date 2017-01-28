

#calss header
class _CONTIGUOUS():
	def __init__(self,): 
		self.name = "CONTIGUOUS"
		self.definitions = [u'next to or touching another, usually similar, thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
