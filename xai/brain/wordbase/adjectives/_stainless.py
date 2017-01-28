

#calss header
class _STAINLESS():
	def __init__(self,): 
		self.name = "STAINLESS"
		self.definitions = [u'with no marks on it, or made of a substance that is not damaged by air or water and that does not change colour: ', u'morally good; having done nothing that could be considered to be wrong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
