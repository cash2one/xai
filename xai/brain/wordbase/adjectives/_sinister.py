

#calss header
class _SINISTER():
	def __init__(self,): 
		self.name = "SINISTER"
		self.definitions = [u'making you feel that something bad or evil might happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
