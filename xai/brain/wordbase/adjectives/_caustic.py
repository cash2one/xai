

#calss header
class _CAUSTIC():
	def __init__(self,): 
		self.name = "CAUSTIC"
		self.definitions = [u'A caustic chemical burns or destroys things, especially anything made of living cells: ', u'A caustic remark or way of speaking is hurtful, critical, or intentionally unkind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
