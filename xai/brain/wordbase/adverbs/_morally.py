

#calss header
class _MORALLY():
	def __init__(self,): 
		self.name = "MORALLY"
		self.definitions = [u'based on principles that you or people in general consider to be right, honest, or acceptable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
