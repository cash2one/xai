

#calss header
class _DOWNSTAIRS():
	def __init__(self,): 
		self.name = "DOWNSTAIRS"
		self.definitions = [u'to or on a lower floor of a building, especially the ground floor: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
