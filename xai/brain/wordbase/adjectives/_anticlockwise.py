

#calss header
class _ANTICLOCKWISE():
	def __init__(self,): 
		self.name = "ANTICLOCKWISE"
		self.definitions = [u'in the opposite direction to the movement of the hands of a clock: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
