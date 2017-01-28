

#calss header
class _OVERTIME():
	def __init__(self,): 
		self.name = "OVERTIME"
		self.definitions = [u'(time spent working) after the usual time needed or expected in a job: ', u'a period of time in a sports game in which play continues if neither team has won in the usual time allowed for the game']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
