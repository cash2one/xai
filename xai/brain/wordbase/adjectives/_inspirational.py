

#calss header
class _INSPIRATIONAL():
	def __init__(self,): 
		self.name = "INSPIRATIONAL"
		self.definitions = [u'making you feel full of hope or encouraged: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
