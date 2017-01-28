

#calss header
class _EXTRAVAGANT():
	def __init__(self,): 
		self.name = "EXTRAVAGANT"
		self.definitions = [u'spending too much money, or using too much of something: ', u'extreme and unreasonable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
