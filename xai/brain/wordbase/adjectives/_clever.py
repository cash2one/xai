

#calss header
class _CLEVER():
	def __init__(self,): 
		self.name = "CLEVER"
		self.definitions = [u'having or showing the ability to learn and understand things quickly and easily: ', u'skilful: ', u'well-designed: ', u'showing intelligence, but not sincere, polite, or serious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
