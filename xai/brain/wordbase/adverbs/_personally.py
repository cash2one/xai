

#calss header
class _PERSONALLY():
	def __init__(self,): 
		self.name = "PERSONALLY"
		self.definitions = [u'used when you give your opinion: ', u'affecting you and not anyone else: ', u'done by you and not by someone else: ', u'to think that someone is offending you when they are not: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
