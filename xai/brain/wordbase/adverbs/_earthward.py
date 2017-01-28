

#calss header
class _EARTHWARD():
	def __init__(self,): 
		self.name = "EARTHWARD"
		self.definitions = [u'towards the earth, from the air or from space: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
