

#calss header
class _INIMITABLE():
	def __init__(self,): 
		self.name = "INIMITABLE"
		self.definitions = [u'very unusual or of very high quality and therefore impossible to copy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
