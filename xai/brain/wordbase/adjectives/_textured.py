

#calss header
class _TEXTURED():
	def __init__(self,): 
		self.name = "TEXTURED"
		self.definitions = [u'having a surface that is not smooth but with a raised pattern: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
