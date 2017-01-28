

#calss header
class _CULPABLE():
	def __init__(self,): 
		self.name = "CULPABLE"
		self.definitions = [u'deserving to be blamed or considered responsible for something bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
