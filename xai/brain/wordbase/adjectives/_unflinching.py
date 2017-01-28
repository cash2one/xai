

#calss header
class _UNFLINCHING():
	def __init__(self,): 
		self.name = "UNFLINCHING"
		self.definitions = [u'not frightened of or not trying to avoid something dangerous or unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
