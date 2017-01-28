

#calss header
class _COMFORTABLY():
	def __init__(self,): 
		self.name = "COMFORTABLY"
		self.definitions = [u'in a comfortable way: ', u'without financial or other problems: ', u'having enough money to lead a good life']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
