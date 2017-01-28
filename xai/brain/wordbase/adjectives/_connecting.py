

#calss header
class _CONNECTING():
	def __init__(self,): 
		self.name = "CONNECTING"
		self.definitions = [u'joining or being joined: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
