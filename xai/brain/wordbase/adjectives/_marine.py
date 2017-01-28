

#calss header
class _MARINE():
	def __init__(self,): 
		self.name = "MARINE"
		self.definitions = [u'related to the sea or sea transport: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
