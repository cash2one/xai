

#calss header
class _TITLED():
	def __init__(self,): 
		self.name = "TITLED"
		self.definitions = [u'with the title of: ', u'A person who is titled has a special word, such as Sir or Lady, before their own name, showing that they have a high social rank: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
