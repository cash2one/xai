

#calss header
class _MENTALLY():
	def __init__(self,): 
		self.name = "MENTALLY"
		self.definitions = [u'connected with or related to the mind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
