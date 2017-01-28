

#calss header
class _INSOLVENT():
	def __init__(self,): 
		self.name = "INSOLVENT"
		self.definitions = [u'(especially of a company) not having enough money to pay debts, buy goods, etc.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
