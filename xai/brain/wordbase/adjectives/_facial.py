

#calss header
class _FACIAL():
	def __init__(self,): 
		self.name = "FACIAL"
		self.definitions = [u'of or on the face: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
