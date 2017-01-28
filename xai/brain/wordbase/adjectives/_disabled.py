

#calss header
class _DISABLED():
	def __init__(self,): 
		self.name = "DISABLED"
		self.definitions = [u'not having one or more of the physical or mental abilities that most people have: ', u'specially relating to or intended for disabled people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
