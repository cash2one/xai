

#calss header
class _MISOGYNIST():
	def __init__(self,): 
		self.name = "MISOGYNIST"
		self.definitions = [u'showing feelings of hating women or a belief that men are much better than women: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
