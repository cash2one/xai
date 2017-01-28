

#calss header
class _MOROSE():
	def __init__(self,): 
		self.name = "MOROSE"
		self.definitions = [u'unhappy, annoyed, and unwilling to speak or smile: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
