

#calss header
class _EQUAL():
	def __init__(self,): 
		self.name = "EQUAL"
		self.definitions = [u'the same in amount, number, or size: ', u'the same in importance and deserving the same treatment: ', u'skilled or brave enough for a difficult duty or piece of work: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
