

#calss header
class _BAGGY():
	def __init__(self,): 
		self.name = "BAGGY"
		self.definitions = [u'(of clothes) hanging loosely because of being too big or having been stretched: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
