

#calss header
class _CENTRALLY():
	def __init__(self,): 
		self.name = "CENTRALLY"
		self.definitions = [u'in, at, from, or near the centre or most important part of something: ', u'from one main place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
