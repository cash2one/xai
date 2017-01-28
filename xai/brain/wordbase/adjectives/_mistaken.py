

#calss header
class _MISTAKEN():
	def __init__(self,): 
		self.name = "MISTAKEN"
		self.definitions = [u'wrong in what you believe, or based on a belief that is wrong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
