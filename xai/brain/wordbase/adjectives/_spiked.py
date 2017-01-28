

#calss header
class _SPIKED():
	def __init__(self,): 
		self.name = "SPIKED"
		self.definitions = [u'with a sharp point or points: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
