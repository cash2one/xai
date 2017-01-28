

#calss header
class _MONSTROUS():
	def __init__(self,): 
		self.name = "MONSTROUS"
		self.definitions = [u'very cruel: ', u'like a monster: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
