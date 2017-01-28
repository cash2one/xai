

#calss header
class _TRADITIONAL():
	def __init__(self,): 
		self.name = "TRADITIONAL"
		self.definitions = [u'following or belonging to the customs or ways of behaving that have continued in a group of people or society for a long time without changing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
