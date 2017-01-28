

#calss header
class _MANICURED():
	def __init__(self,): 
		self.name = "MANICURED"
		self.definitions = [u'having had a manicure: ', u'If something, such as a garden, is manicured, it is well cared for and looks very tidy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
