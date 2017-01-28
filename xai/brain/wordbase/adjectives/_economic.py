

#calss header
class _ECONOMIC():
	def __init__(self,): 
		self.name = "ECONOMIC"
		self.definitions = [u'relating to trade, industry, and money: ', u'making a profit, or likely to make a profit: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
