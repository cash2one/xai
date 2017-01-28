

#calss header
class _UNTUTORED():
	def __init__(self,): 
		self.name = "UNTUTORED"
		self.definitions = [u'having no knowledge of or education in a particular subject', u'if or because you are, I am, etc. an untutored person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
