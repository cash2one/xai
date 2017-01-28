

#calss header
class _UPSTAGE():
	def __init__(self,): 
		self.name = "UPSTAGE"
		self.definitions = [u'towards or at the part of a theatre stage that is furthest from the people watching the performance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
