

#calss header
class _POSTGRADUATE():
	def __init__(self,): 
		self.name = "POSTGRADUATE"
		self.definitions = [u'used to refer to university studies or students at a more advanced level than a first degree: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
