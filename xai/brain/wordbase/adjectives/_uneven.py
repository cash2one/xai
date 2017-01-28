

#calss header
class _UNEVEN():
	def __init__(self,): 
		self.name = "UNEVEN"
		self.definitions = [u'not level, equal, flat, or continuous: ', u'different in quality; often used to avoid saying bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
