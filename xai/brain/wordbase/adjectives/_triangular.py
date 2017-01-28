

#calss header
class _TRIANGULAR():
	def __init__(self,): 
		self.name = "TRIANGULAR"
		self.definitions = [u'shaped like a triangle: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
