

#calss header
class _ROUGHLY():
	def __init__(self,): 
		self.name = "ROUGHLY"
		self.definitions = [u'approximately: ', u'without taking a lot of care to make something perfect: ', u'in a violent or angry way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
