

#calss header
class _TRANSPARENT():
	def __init__(self,): 
		self.name = "TRANSPARENT"
		self.definitions = [u'If a substance or object is transparent, you can see through it very clearly: ', u'clear and easy to understand or recognize: ', u'open and honest, without secrets: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
