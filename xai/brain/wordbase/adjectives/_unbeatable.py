

#calss header
class _UNBEATABLE():
	def __init__(self,): 
		self.name = "UNBEATABLE"
		self.definitions = [u'unable to be defeated or improved because of excellent quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
