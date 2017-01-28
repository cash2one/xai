

#calss header
class _OVERPAID():
	def __init__(self,): 
		self.name = "OVERPAID"
		self.definitions = [u'paid too much or more than usual: ', u'paid more than necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
