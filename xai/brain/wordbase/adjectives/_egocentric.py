

#calss header
class _EGOCENTRIC():
	def __init__(self,): 
		self.name = "EGOCENTRIC"
		self.definitions = [u'thinking only about yourself and what is good for you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
