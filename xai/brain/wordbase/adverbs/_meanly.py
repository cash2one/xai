

#calss header
class _MEANLY():
	def __init__(self,): 
		self.name = "MEANLY"
		self.definitions = [u'in a way that is unkind towards other people: ', u'in a way that shows that you are not willing to give or share things, especially money']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
