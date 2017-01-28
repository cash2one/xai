

#calss header
class _FRAUGHT():
	def __init__(self,): 
		self.name = "FRAUGHT"
		self.definitions = [u'full of unpleasant things such as problems or dangers: ', u'causing or having extreme worry or anxiety: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
