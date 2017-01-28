

#calss header
class _NOMINAL():
	def __init__(self,): 
		self.name = "NOMINAL"
		self.definitions = [u'in name or thought but not in fact or not as things really are: ', u'A nominal amount of money is very small compared to an expected price or value: ', u'relating to a noun']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
