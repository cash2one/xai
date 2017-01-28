

#calss header
class _THOROUGH():
	def __init__(self,): 
		self.name = "THOROUGH"
		self.definitions = [u'detailed and careful: ', u'complete, very great, or very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
