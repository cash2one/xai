

#calss header
class _MURDEROUS():
	def __init__(self,): 
		self.name = "MURDEROUS"
		self.definitions = [u'extremely dangerous and likely to commit murder: ', u'extremely unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
