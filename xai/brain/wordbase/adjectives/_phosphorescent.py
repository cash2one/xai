

#calss header
class _PHOSPHORESCENT():
	def __init__(self,): 
		self.name = "PHOSPHORESCENT"
		self.definitions = [u'giving off light after radiation has hit it']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
