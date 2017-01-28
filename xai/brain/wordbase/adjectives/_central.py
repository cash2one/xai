

#calss header
class _CENTRAL():
	def __init__(self,): 
		self.name = "CENTRAL"
		self.definitions = [u'in, at, from, or near the centre or most important part of something: ', u'main or important: ', u'controlled or organized in one main place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
