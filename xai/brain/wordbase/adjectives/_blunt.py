

#calss header
class _BLUNT():
	def __init__(self,): 
		self.name = "BLUNT"
		self.definitions = [u'A blunt pencil, knife, etc. is not sharp and therefore not able to write, cut, etc. well.', u"saying what you think without trying to be polite or considering other people's feelings: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
