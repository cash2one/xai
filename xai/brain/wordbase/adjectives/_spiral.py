

#calss header
class _SPIRAL():
	def __init__(self,): 
		self.name = "SPIRAL"
		self.definitions = [u'shaped in a series of curves, each one above or wider than the one before: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
