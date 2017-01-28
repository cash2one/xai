

#calss header
class _DEPRESSINGLY():
	def __init__(self,): 
		self.name = "DEPRESSINGLY"
		self.definitions = [u'in a way that makes you feel unhappy and without hope for the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
