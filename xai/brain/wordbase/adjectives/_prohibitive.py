

#calss header
class _PROHIBITIVE():
	def __init__(self,): 
		self.name = "PROHIBITIVE"
		self.definitions = [u'If the cost of something is prohibitive, it is too expensive for most people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
