

#calss header
class _AMISS():
	def __init__(self,): 
		self.name = "AMISS"
		self.definitions = [u'wrong, not suitable, or not as expected: ', u'If something might/would not go amiss, it would be useful and might help to improve a situation: ', u'to be offended by something that someone has said to you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
