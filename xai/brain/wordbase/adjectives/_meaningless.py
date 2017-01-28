

#calss header
class _MEANINGLESS():
	def __init__(self,): 
		self.name = "MEANINGLESS"
		self.definitions = [u'having no meaning: ', u'having no importance or value: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
