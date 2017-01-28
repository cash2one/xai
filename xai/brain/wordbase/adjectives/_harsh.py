

#calss header
class _HARSH():
	def __init__(self,): 
		self.name = "HARSH"
		self.definitions = [u'unpleasant, unkind, cruel, or more severe than is necessary: ', u'too strong, bright, loud, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
