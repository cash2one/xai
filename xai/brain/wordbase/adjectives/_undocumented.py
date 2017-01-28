

#calss header
class _UNDOCUMENTED():
	def __init__(self,): 
		self.name = "UNDOCUMENTED"
		self.definitions = [u'not supported by written proof: ', u'not having any documents to prove that you are living or working in a country legally: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
