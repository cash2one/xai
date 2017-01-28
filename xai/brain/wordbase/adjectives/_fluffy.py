

#calss header
class _FLUFFY():
	def __init__(self,): 
		self.name = "FLUFFY"
		self.definitions = [u'soft and like wool or like fur: ', u'light and full of air: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
