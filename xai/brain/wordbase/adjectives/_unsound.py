

#calss header
class _UNSOUND():
	def __init__(self,): 
		self.name = "UNSOUND"
		self.definitions = [u"If a person's activities or judgment are unsound, they are not good enough, acceptable, or able to be trusted: ", u'If a building or other structure is unsound, it is in bad condition and likely to fall down or fail: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
