

#calss header
class _IRREPRESSIBLE():
	def __init__(self,): 
		self.name = "IRREPRESSIBLE"
		self.definitions = [u'full of energy and enthusiasm; impossible to stop: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
