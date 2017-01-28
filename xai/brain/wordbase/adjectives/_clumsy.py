

#calss header
class _CLUMSY():
	def __init__(self,): 
		self.name = "CLUMSY"
		self.definitions = [u'awkward in movement or manner: ', u'A clumsy person often has accidents because they do not behave in a careful, controlled way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
