

#calss header
class _UNCORROBORATED():
	def __init__(self,): 
		self.name = "UNCORROBORATED"
		self.definitions = [u'Uncorroborated information has not been proven to be true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
