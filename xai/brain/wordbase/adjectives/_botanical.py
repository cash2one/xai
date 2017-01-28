

#calss header
class _BOTANICAL():
	def __init__(self,): 
		self.name = "BOTANICAL"
		self.definitions = [u'involving or relating to plants or the study of plants: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
