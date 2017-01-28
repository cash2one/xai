

#calss header
class _ROTUND():
	def __init__(self,): 
		self.name = "ROTUND"
		self.definitions = [u'(especially of a person) round or rounded in shape']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
