

#calss header
class _SUPERCILIOUS():
	def __init__(self,): 
		self.name = "SUPERCILIOUS"
		self.definitions = [u'behaving as if you are better than other people, and that their opinions, beliefs, or ideas are not important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
