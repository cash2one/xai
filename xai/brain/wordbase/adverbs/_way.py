

#calss header
class _WAY():
	def __init__(self,): 
		self.name = "WAY"
		self.definitions = [u'used to emphasize degree or separation, especially in space or time: ', u'in the direction of: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
