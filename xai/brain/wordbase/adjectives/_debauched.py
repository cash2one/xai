

#calss header
class _DEBAUCHED():
	def __init__(self,): 
		self.name = "DEBAUCHED"
		self.definitions = [u'made weaker or destroyed by bad sexual behaviour, drinking too much alcohol, taking drugs, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
