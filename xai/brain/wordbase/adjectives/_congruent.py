

#calss header
class _CONGRUENT():
	def __init__(self,): 
		self.name = "CONGRUENT"
		self.definitions = [u'similar to or in agreement with something, so that the two things can both exist or can be combined without problems: ', u'used to refer to a shape in mathematics that has the same shape and size as another: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
