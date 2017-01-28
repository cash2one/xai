

#calss header
class _DAMN():
	def __init__(self,): 
		self.name = "DAMN"
		self.definitions = [u'used to express anger with someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
