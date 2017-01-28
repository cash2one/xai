

#calss header
class _RIGHTFUL():
	def __init__(self,): 
		self.name = "RIGHTFUL"
		self.definitions = [u'A rightful position or claim is one that is morally or legally correct: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
