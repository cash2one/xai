

#calss header
class _TACITURN():
	def __init__(self,): 
		self.name = "TACITURN"
		self.definitions = [u'tending not to speak much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
