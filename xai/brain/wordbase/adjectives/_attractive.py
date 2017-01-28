

#calss header
class _ATTRACTIVE():
	def __init__(self,): 
		self.name = "ATTRACTIVE"
		self.definitions = [u'very pleasing in appearance or sound: ', u'causing interest or pleasure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
