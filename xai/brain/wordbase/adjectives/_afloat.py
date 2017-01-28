

#calss header
class _AFLOAT():
	def __init__(self,): 
		self.name = "AFLOAT"
		self.definitions = [u'floating on water: ', u'having enough money to pay what you owe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
