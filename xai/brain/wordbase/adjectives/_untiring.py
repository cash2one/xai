

#calss header
class _UNTIRING():
	def __init__(self,): 
		self.name = "UNTIRING"
		self.definitions = [u'If someone has untiring energy, interest, or enthusiasm, their energy, interest, or enthusiasm never becomes weaker: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
