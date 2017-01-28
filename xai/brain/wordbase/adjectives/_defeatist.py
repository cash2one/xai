

#calss header
class _DEFEATIST():
	def __init__(self,): 
		self.name = "DEFEATIST"
		self.definitions = [u'having no hope and expecting to fail: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
