

#calss header
class _IMMINENT():
	def __init__(self,): 
		self.name = "IMMINENT"
		self.definitions = [u'coming or likely to happen very soon: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
