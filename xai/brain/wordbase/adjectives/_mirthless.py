

#calss header
class _MIRTHLESS():
	def __init__(self,): 
		self.name = "MIRTHLESS"
		self.definitions = [u'not showing real enjoyment or happiness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
