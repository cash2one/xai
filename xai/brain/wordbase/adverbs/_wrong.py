

#calss header
class _WRONG():
	def __init__(self,): 
		self.name = "WRONG"
		self.definitions = [u'in a way that is not correct: ', u'to make a mistake in the way you answer or understand something: ', u'If a situation or event goes wrong, it becomes unpleasant and is not a success: ', u'to make a mistake: ', u'If a machine goes wrong, it stops working correctly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
