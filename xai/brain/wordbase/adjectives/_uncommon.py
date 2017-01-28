

#calss header
class _UNCOMMON():
	def __init__(self,): 
		self.name = "UNCOMMON"
		self.definitions = [u'not seen, happening, or experienced often: ', u'An uncommon quality, especially a human quality, is larger in amount or degree than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
