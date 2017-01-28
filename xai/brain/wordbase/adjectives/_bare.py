

#calss header
class _BARE():
	def __init__(self,): 
		self.name = "BARE"
		self.definitions = [u'without any clothes or not covered by anything: ', u'only the most basic or important: ', u'the least possible amount: ', u'the most basic things that you need in order to live or to do something: ', u'If a cupboard or room is bare, there is nothing in it.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
