

#calss header
class _VALUABLE():
	def __init__(self,): 
		self.name = "VALUABLE"
		self.definitions = [u'worth a lot of money: ', u'Valuable information, advice, etc. is very helpful or important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
