

#calss header
class _STERLING():
	def __init__(self,): 
		self.name = "STERLING"
		self.definitions = [u'(of precious metal, especially silver) of a particular standard of purity: ', u'of a very high standard: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
