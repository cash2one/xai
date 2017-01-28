

#calss header
class _IMPURE():
	def __init__(self,): 
		self.name = "IMPURE"
		self.definitions = [u'mixed with other substances and therefore lower in quality: ', u'involving sexual thoughts or behaviour that are wrong or not moral: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
