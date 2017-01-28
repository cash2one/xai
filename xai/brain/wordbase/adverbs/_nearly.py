

#calss header
class _NEARLY():
	def __init__(self,): 
		self.name = "NEARLY"
		self.definitions = [u'almost, or not completely: ', u'a lot less: ', u'much less than you want or need: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
