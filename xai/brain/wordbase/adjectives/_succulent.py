

#calss header
class _SUCCULENT():
	def __init__(self,): 
		self.name = "SUCCULENT"
		self.definitions = [u'Succulent food is pleasantly juicy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
