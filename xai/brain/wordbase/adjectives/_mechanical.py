

#calss header
class _MECHANICAL():
	def __init__(self,): 
		self.name = "MECHANICAL"
		self.definitions = [u'operated by a machine, or connected with machines or their parts: ', u'relating to movement, or to mechanics (= the study of the effect of physical forces on objects and their movement): ', u'without thinking about what you are doing, especially because you do something often: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
