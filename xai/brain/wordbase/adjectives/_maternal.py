

#calss header
class _MATERNAL():
	def __init__(self,): 
		self.name = "MATERNAL"
		self.definitions = [u'behaving or feeling in the way that a mother does towards her child, especially in a kind, loving way: ', u"related to a mother's side of the family: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
