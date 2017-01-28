

#calss header
class _RIPE():
	def __init__(self,): 
		self.name = "RIPE"
		self.definitions = [u'(of fruit or crops) completely developed and ready to be collected or eaten: ', u'Ripe cheese has developed a strong flavour: ', u'A ripe smell is strong and unpleasant: ', u'used to describe language that is rude: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
