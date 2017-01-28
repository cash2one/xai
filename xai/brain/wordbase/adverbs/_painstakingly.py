

#calss header
class _PAINSTAKINGLY():
	def __init__(self,): 
		self.name = "PAINSTAKINGLY"
		self.definitions = [u'in a way that shows you have taken a lot of care or made a lot of effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
