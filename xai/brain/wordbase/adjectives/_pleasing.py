

#calss header
class _PLEASING():
	def __init__(self,): 
		self.name = "PLEASING"
		self.definitions = [u'giving a feeling of satisfaction or enjoyment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
