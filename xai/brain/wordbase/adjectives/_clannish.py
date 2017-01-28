

#calss header
class _CLANNISH():
	def __init__(self,): 
		self.name = "CLANNISH"
		self.definitions = [u'used to describe members of a group of people or society who are friendly to each other, but not to people outside the group']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
