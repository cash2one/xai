

#calss header
class _FANCIED():
	def __init__(self,): 
		self.name = "FANCIED"
		self.definitions = [u'expected or thought likely to succeed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
