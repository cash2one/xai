

#calss header
class _CRISPY():
	def __init__(self,): 
		self.name = "CRISPY"
		self.definitions = [u'Crispy food is hard enough to be broken easily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
