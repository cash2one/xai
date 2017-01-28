

#calss header
class _BANKRUPT():
	def __init__(self,): 
		self.name = "BANKRUPT"
		self.definitions = [u'unable to pay what you owe, and having had control of your financial matters given, by a law court, to a person who sells your property to pay your debts: ', u'having no money: ', u'not having any good qualities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
