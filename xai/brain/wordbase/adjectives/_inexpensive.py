

#calss header
class _INEXPENSIVE():
	def __init__(self,): 
		self.name = "INEXPENSIVE"
		self.definitions = [u'not costing a lot of money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
