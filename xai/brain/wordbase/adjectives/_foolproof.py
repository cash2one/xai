

#calss header
class _FOOLPROOF():
	def __init__(self,): 
		self.name = "FOOLPROOF"
		self.definitions = [u'(of a plan or machine) so simple and easy to understand that it is unable to go wrong or be used wrongly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
