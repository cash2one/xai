

#calss header
class _FLAT():
	def __init__(self,): 
		self.name = "FLAT"
		self.definitions = [u'(in music) lower than a particular note or the correct note: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
