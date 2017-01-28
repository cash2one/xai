

#calss header
class _SERRATED():
	def __init__(self,): 
		self.name = "SERRATED"
		self.definitions = [u'having a row of sharp points along the edge: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
