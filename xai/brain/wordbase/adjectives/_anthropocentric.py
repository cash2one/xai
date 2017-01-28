

#calss header
class _ANTHROPOCENTRIC():
	def __init__(self,): 
		self.name = "ANTHROPOCENTRIC"
		self.definitions = [u'considering humans and their existence as the most important and central fact in the universe']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
