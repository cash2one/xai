

#calss header
class _BLESSED():
	def __init__(self,): 
		self.name = "BLESSED"
		self.definitions = [u'holy: ', u'bringing you happiness, luck, or something you need: ', u'to be lucky in having a particular thing: ', u'an expression of anger: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
