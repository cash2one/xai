

#calss header
class _RIFE():
	def __init__(self,): 
		self.name = "RIFE"
		self.definitions = [u'If something unpleasant is rife, it is very common or happens a lot: ', u'full of something unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
