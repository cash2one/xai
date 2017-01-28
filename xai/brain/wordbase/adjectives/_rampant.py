

#calss header
class _RAMPANT():
	def __init__(self,): 
		self.name = "RAMPANT"
		self.definitions = [u'(of something bad) getting worse quickly and in an uncontrolled way: ', u'(of an animal represented on a coat of arms) standing on its back legs with its front legs raised: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
