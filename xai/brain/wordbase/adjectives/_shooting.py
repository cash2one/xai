

#calss header
class _SHOOTING():
	def __init__(self,): 
		self.name = "SHOOTING"
		self.definitions = [u'(of prices) rising very quickly to a high level']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
