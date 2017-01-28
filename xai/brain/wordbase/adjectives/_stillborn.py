

#calss header
class _STILLBORN():
	def __init__(self,): 
		self.name = "STILLBORN"
		self.definitions = [u'born dead: ', u'If an idea or event is stillborn, it is unsuccessful or does not happen.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
