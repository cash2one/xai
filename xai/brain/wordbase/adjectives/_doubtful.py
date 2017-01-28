

#calss header
class _DOUBTFUL():
	def __init__(self,): 
		self.name = "DOUBTFUL"
		self.definitions = [u'If you are doubtful about something, you are uncertain about it: ', u'If a situation is doubtful, it is unlikely to happen or to be successful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
