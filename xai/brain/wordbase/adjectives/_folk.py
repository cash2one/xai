

#calss header
class _FOLK():
	def __init__(self,): 
		self.name = "FOLK"
		self.definitions = [u'traditional to or typical of a particular group or country, especially one where people mainly live in the countryside, and usually passed on from parents to their children over a long period of time: ', u'Folk art expresses something about the lives and feelings of ordinary people in a particular group or country, especially those living in the countryside: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
