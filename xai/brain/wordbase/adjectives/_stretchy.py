

#calss header
class _STRETCHY():
	def __init__(self,): 
		self.name = "STRETCHY"
		self.definitions = [u'Stretchy material stretches or can be stretched: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
