

#calss header
class _GENIAL():
	def __init__(self,): 
		self.name = "GENIAL"
		self.definitions = [u'friendly and pleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
