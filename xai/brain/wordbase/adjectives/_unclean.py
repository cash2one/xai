

#calss header
class _UNCLEAN():
	def __init__(self,): 
		self.name = "UNCLEAN"
		self.definitions = [u'not clean and therefore likely to cause disease: ', u'not clean or pure, or morally bad, as described by the rules of a religion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
