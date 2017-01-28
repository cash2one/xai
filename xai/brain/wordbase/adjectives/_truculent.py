

#calss header
class _TRUCULENT():
	def __init__(self,): 
		self.name = "TRUCULENT"
		self.definitions = [u'unpleasant and likely to argue a lot: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
