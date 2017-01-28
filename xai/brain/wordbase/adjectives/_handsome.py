

#calss header
class _HANDSOME():
	def __init__(self,): 
		self.name = "HANDSOME"
		self.definitions = [u'A handsome man is physically attractive in a traditional, male way: ', u'A handsome woman is attractive in a strong way: ', u'large in amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
