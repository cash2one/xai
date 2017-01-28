

#calss header
class _UNDERFUNDED():
	def __init__(self,): 
		self.name = "UNDERFUNDED"
		self.definitions = [u'If an organization is underfunded, it does not receive a large enough income: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
