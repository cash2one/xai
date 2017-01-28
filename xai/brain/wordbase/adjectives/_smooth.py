

#calss header
class _SMOOTH():
	def __init__(self,): 
		self.name = "SMOOTH"
		self.definitions = [u'having a surface or consisting of a substance that is perfectly regular and has no holes, lumps, or areas that rise or fall suddenly: ', u'happening without any sudden changes, interruption, or difficulty: ', u'having a pleasant flavour that is not sour or bitter: ', u'very polite, confident, and able to persuade people, but in a way that is not sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
