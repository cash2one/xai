

#calss header
class _FIRST():
	def __init__(self,): 
		self.name = "FIRST"
		self.definitions = [u'before all others in order, time, amount, quality, or importance: ', u'for the first time: ', u'used at the beginning of a list of things you want to say or write: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
