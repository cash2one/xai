

#calss header
class _WOODEN():
	def __init__(self,): 
		self.name = "WOODEN"
		self.definitions = [u'made of wood: ', u'used to describe behaviour that is awkward or shows little expression: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
