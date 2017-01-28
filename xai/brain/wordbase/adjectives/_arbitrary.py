

#calss header
class _ARBITRARY():
	def __init__(self,): 
		self.name = "ARBITRARY"
		self.definitions = [u'based on chance rather than being planned or based on reason: ', u"using unlimited personal power without considering other people's wishes: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
