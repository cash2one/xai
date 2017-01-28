

#calss header
class _FUGITIVE():
	def __init__(self,): 
		self.name = "FUGITIVE"
		self.definitions = [u'(especially of thoughts or feelings) lasting for only a short time: ', u'relating to a fugitive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
