

#calss header
class _THUS():
	def __init__(self,): 
		self.name = "THUS"
		self.definitions = [u'in this way: ', u'with this result: ', u'as far as this or until now: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
