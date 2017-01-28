

#calss header
class _BRASSY():
	def __init__(self,): 
		self.name = "BRASSY"
		self.definitions = [u'like brass in colour, or too bright: ', u'loud and unpleasant: ', u'used to describe a woman who speaks and laughs too loudly and who dresses in bright, cheap clothes, often wearing too much make-up: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
