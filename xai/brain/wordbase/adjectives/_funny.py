

#calss header
class _FUNNY():
	def __init__(self,): 
		self.name = "FUNNY"
		self.definitions = [u'humorous; causing laughter: ', u'strange, surprising, unexpected, or difficult to explain or understand: ', u'dishonest; involving cheating: ', u'unfriendly or seeming to be offended: ', u'slightly ill: ', u'slightly crazy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
