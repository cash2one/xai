

#calss header
class _EXPEDIENT():
	def __init__(self,): 
		self.name = "EXPEDIENT"
		self.definitions = [u'helpful or useful in a particular situation, but sometimes not morally acceptable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
