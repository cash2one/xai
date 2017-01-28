

#calss header
class _RARE():
	def __init__(self,): 
		self.name = "RARE"
		self.definitions = [u'not common; very unusual: ', u'(of meat) not cooked for very long and still red: ', u'used to describe the air at the top of a mountain, which contains less oxygen, making it harder to breathe']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
