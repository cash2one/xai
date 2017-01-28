

#calss header
class _STRIKING():
	def __init__(self,): 
		self.name = "STRIKING"
		self.definitions = [u'very unusual or easily noticed, and therefore attracting a lot of attention: ', u'more attractive than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
