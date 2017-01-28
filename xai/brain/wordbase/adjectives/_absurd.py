

#calss header
class _ABSURD():
	def __init__(self,): 
		self.name = "ABSURD"
		self.definitions = [u'stupid and unreasonable, or silly in a humorous way: ', u'things that happen that are stupid or unreasonable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
