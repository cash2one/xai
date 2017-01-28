

#calss header
class _WARRING():
	def __init__(self,): 
		self.name = "WARRING"
		self.definitions = [u'Warring countries or groups of people are at war with each other: ', u'Warring groups disagree and argue strongly with each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
