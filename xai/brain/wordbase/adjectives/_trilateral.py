

#calss header
class _TRILATERAL():
	def __init__(self,): 
		self.name = "TRILATERAL"
		self.definitions = [u'involving three groups or countries: ', u'having three sides: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
