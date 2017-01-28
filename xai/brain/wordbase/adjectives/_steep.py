

#calss header
class _STEEP():
	def __init__(self,): 
		self.name = "STEEP"
		self.definitions = [u'(of a slope) rising or falling at a sharp angle: ', u'A steep rise or fall is one that goes very quickly from low to high or from high to low: ', u'(especially of prices) too much, or more than is reasonable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
