

#calss header
class _FABULOUS():
	def __init__(self,): 
		self.name = "FABULOUS"
		self.definitions = [u'very good; excellent: ', u'imaginary, not existing in real life: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
