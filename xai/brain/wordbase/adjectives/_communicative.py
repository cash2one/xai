

#calss header
class _COMMUNICATIVE():
	def __init__(self,): 
		self.name = "COMMUNICATIVE"
		self.definitions = [u'willing to talk to people and give them information: ', u'relating to communication: ', u'relating to a style of language teaching in which interaction (= talking and responding) is seen as the most important method of learning, and the main aim of learning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
