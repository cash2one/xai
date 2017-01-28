

#calss header
class _BROADLY():
	def __init__(self,): 
		self.name = "BROADLY"
		self.definitions = [u'in a general way, without considering specific examples or all the details: ', u'If someone smiles broadly, they have a big smile: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
