

#calss header
class _SOPHISTICATED():
	def __init__(self,): 
		self.name = "SOPHISTICATED"
		self.definitions = [u'having a good understanding of the way people behave and/or a good knowledge of culture and fashion: ', u'intelligent or made in a complicated way and therefore able to do complicated tasks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
