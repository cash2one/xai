

#calss header
class _SAUCY():
	def __init__(self,): 
		self.name = "SAUCY"
		self.definitions = [u'rude and showing no respect, or referring to sex, especially in a humorous way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
