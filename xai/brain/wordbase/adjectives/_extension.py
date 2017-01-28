

#calss header
class _EXTENSION():
	def __init__(self,): 
		self.name = "EXTENSION"
		self.definitions = [u"intended to support students' learning by making them try different or more difficult things in addition to their basic work: ", u'offered by a university to people who are not studying for a degree there : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
