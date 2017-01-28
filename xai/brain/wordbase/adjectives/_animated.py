

#calss header
class _ANIMATED():
	def __init__(self,): 
		self.name = "ANIMATED"
		self.definitions = [u'full of interest and energy: ', u'Animated films, drawings, models, etc. are ones that are photographed or created by a computer and shown in a way that makes them move.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
