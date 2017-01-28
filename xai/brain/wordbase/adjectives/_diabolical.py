

#calss header
class _DIABOLICAL():
	def __init__(self,): 
		self.name = "DIABOLICAL"
		self.definitions = [u'extremely bad or shocking: ', u'evil, or caused by the Devil']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
