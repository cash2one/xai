

#calss header
class _SUBDUED():
	def __init__(self,): 
		self.name = "SUBDUED"
		self.definitions = [u'If a colour or light is subdued, it is not very bright: ', u'If a noise is subdued, it is not loud: ', u'If a person is subdued, they are not as happy as usual or they are quieter than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
