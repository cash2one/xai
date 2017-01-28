

#calss header
class _CLOCKWISE():
	def __init__(self,): 
		self.name = "CLOCKWISE"
		self.definitions = [u'in the direction in which the hands (= thin parts that point) of a clock move: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
