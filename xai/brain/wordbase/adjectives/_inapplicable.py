

#calss header
class _INAPPLICABLE():
	def __init__(self,): 
		self.name = "INAPPLICABLE"
		self.definitions = [u'not directed at, intended for, or suitable for someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
