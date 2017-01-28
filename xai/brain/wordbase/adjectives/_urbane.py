

#calss header
class _URBANE():
	def __init__(self,): 
		self.name = "URBANE"
		self.definitions = [u'(especially of a man) confident, comfortable, and polite in social situations: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
