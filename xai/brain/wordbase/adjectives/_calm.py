

#calss header
class _CALM():
	def __init__(self,): 
		self.name = "CALM"
		self.definitions = [u'peaceful, quiet, and without worry: ', u'without hurried movement or noise: ', u'If the weather is calm, there is no wind, or if the sea or a lake is calm, it is still and has no waves.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
