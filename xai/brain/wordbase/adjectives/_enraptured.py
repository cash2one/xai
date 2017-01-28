

#calss header
class _ENRAPTURED():
	def __init__(self,): 
		self.name = "ENRAPTURED"
		self.definitions = [u'filled with great pleasure or extremely pleased by something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
