

#calss header
class _SHOPWORN():
	def __init__(self,): 
		self.name = "SHOPWORN"
		self.definitions = [u'If goods sold in shops are shopworn, they are slightly dirty or damaged and therefore reduced in price', u'If a story or joke is shopworn, it is boring or not interesting because it is so familiar to people.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
