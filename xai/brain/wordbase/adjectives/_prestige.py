

#calss header
class _PRESTIGE():
	def __init__(self,): 
		self.name = "PRESTIGE"
		self.definitions = [u'causing admiration because of being connected with being rich or powerful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
