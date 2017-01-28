

#calss header
class _ROVING():
	def __init__(self,): 
		self.name = "ROVING"
		self.definitions = [u'travelling from place to place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
