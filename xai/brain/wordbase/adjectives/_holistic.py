

#calss header
class _HOLISTIC():
	def __init__(self,): 
		self.name = "HOLISTIC"
		self.definitions = [u'dealing with or treating the whole of something or someone and not just a part: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
