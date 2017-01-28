

#calss header
class _WORTHLESS():
	def __init__(self,): 
		self.name = "WORTHLESS"
		self.definitions = [u'having no value in money: ', u'not important or not useful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
