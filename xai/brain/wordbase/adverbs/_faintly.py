

#calss header
class _FAINTLY():
	def __init__(self,): 
		self.name = "FAINTLY"
		self.definitions = [u'slightly or not strongly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
