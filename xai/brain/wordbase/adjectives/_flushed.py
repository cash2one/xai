

#calss header
class _FLUSHED():
	def __init__(self,): 
		self.name = "FLUSHED"
		self.definitions = [u'red in the face: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
