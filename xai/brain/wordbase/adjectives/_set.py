

#calss header
class _SET():
	def __init__(self,): 
		self.name = "SET"
		self.definitions = [u'ready and prepared: ', u'likely or in a suitable condition: ', u'always the same, never changing: ', u'a phrase in which the words are always used in the same order', u'a set book is one that must be studied for a particular course: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
