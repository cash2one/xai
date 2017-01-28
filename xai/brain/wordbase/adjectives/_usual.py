

#calss header
class _USUAL():
	def __init__(self,): 
		self.name = "USUAL"
		self.definitions = [u'normal; happening, done, or used most often: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
