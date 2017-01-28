

#calss header
class _FORE():
	def __init__(self,): 
		self.name = "FORE"
		self.definitions = [u'(especially on ships) towards or in the front']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
