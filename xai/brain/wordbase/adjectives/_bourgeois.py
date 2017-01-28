

#calss header
class _BOURGEOIS():
	def __init__(self,): 
		self.name = "BOURGEOIS"
		self.definitions = [u'belonging to or typical of the middle class (= a social group between the rich and the poor) especially in supporting existing customs and values, or in having a strong interest in money and possessions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
