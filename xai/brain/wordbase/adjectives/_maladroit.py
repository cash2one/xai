

#calss header
class _MALADROIT():
	def __init__(self,): 
		self.name = "MALADROIT"
		self.definitions = [u'awkward in movement or unskilled in behaviour or action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
