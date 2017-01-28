

#calss header
class _UNCONSIDERED():
	def __init__(self,): 
		self.name = "UNCONSIDERED"
		self.definitions = [u'(of an action or remark) not carefully thought about']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
