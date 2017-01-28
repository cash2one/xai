

#calss header
class _AGHAST():
	def __init__(self,): 
		self.name = "AGHAST"
		self.definitions = [u'suddenly filled with strong feelings of shock and worry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
