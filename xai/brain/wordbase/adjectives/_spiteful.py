

#calss header
class _SPITEFUL():
	def __init__(self,): 
		self.name = "SPITEFUL"
		self.definitions = [u'wanting to annoy, upset, or hurt another person, especially in a small way, because you feel angry towards them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
