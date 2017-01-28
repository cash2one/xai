

#calss header
class _AIRY():
	def __init__(self,): 
		self.name = "AIRY"
		self.definitions = [u'with a lot of light and space: ', u'delicate, as if full of air: ', u'showing no worry or serious thought: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
