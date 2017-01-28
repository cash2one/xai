

#calss header
class _SHADOWY():
	def __init__(self,): 
		self.name = "SHADOWY"
		self.definitions = [u'dark and full of shadows: ', u'used to refer to someone or something about which little is known: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
