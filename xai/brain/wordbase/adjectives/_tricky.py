

#calss header
class _TRICKY():
	def __init__(self,): 
		self.name = "TRICKY"
		self.definitions = [u'If a piece of work or problem is tricky, it is difficult to deal with and needs careful attention or skill: ', u'likely to deceive people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
