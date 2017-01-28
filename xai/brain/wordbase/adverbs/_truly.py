

#calss header
class _TRULY():
	def __init__(self,): 
		self.name = "TRULY"
		self.definitions = [u'used to emphasize that what you are saying is true: ', u'really existing; in fact: ', u'sincerely: ', u'used to end a letter: ', u'in an exact way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
