

#calss header
class _PERFORATED():
	def __init__(self,): 
		self.name = "PERFORATED"
		self.definitions = [u'If paper or another material is perforated, it has a series of small holes made in it, often so that it will tear easily or allow light or air to enter: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
