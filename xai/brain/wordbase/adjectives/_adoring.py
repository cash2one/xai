

#calss header
class _ADORING():
	def __init__(self,): 
		self.name = "ADORING"
		self.definitions = [u'showing very strong love for someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
