

#calss header
class _UNRESTRICTED():
	def __init__(self,): 
		self.name = "UNRESTRICTED"
		self.definitions = [u'not limited or controlled by rules or laws: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
