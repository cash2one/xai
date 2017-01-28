

#calss header
class _HEAVENLY():
	def __init__(self,): 
		self.name = "HEAVENLY"
		self.definitions = [u'of heaven: ', u'giving great pleasure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
