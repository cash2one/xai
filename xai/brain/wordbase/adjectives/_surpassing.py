

#calss header
class _SURPASSING():
	def __init__(self,): 
		self.name = "SURPASSING"
		self.definitions = [u'extremely great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
