

#calss header
class _ACCORDINGLY():
	def __init__(self,): 
		self.name = "ACCORDINGLY"
		self.definitions = [u'in a way that is suitable or right for the situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
