

#calss header
class _BRITANNIC():
	def __init__(self,): 
		self.name = "BRITANNIC"
		self.definitions = [u'British: ', u'the Queen/King of the United Kingdom']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
