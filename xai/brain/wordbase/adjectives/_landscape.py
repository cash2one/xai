

#calss header
class _LANDSCAPE():
	def __init__(self,): 
		self.name = "LANDSCAPE"
		self.definitions = [u'A landscape document is to be printed with the longer side of the paper at the top and bottom.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
