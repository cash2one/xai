

#calss header
class _SKINNY():
	def __init__(self,): 
		self.name = "SKINNY"
		self.definitions = [u'very thin: ', u'low in fat; used especially of coffee made with low-fat milk: ', u': ', u'narrow and fitting closely to the body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
