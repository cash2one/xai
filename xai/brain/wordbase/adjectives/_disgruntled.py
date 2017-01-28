

#calss header
class _DISGRUNTLED():
	def __init__(self,): 
		self.name = "DISGRUNTLED"
		self.definitions = [u'unhappy, annoyed, and disappointed about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
