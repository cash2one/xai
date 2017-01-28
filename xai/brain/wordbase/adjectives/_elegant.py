

#calss header
class _ELEGANT():
	def __init__(self,): 
		self.name = "ELEGANT"
		self.definitions = [u'graceful and attractive in appearance or behaviour: ', u'An elegant idea, plan, or solution is clever but simple, and therefore attractive.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
