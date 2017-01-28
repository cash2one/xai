

#calss header
class _BUTTERY():
	def __init__(self,): 
		self.name = "BUTTERY"
		self.definitions = [u'containing or spread with a lot of butter, or tasting of butter: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
