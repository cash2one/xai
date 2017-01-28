

#calss header
class _PRESUMABLY():
	def __init__(self,): 
		self.name = "PRESUMABLY"
		self.definitions = [u'used to say what you think is the likely situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
