

#calss header
class _MASCULINE():
	def __init__(self,): 
		self.name = "MASCULINE"
		self.definitions = [u'having characteristics that are traditionally thought to be typical of or suitable for men: ', u'belonging to the group of nouns, pronouns, etc. that are not feminine or neuter: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
