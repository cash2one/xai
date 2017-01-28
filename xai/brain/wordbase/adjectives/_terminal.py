

#calss header
class _TERMINAL():
	def __init__(self,): 
		self.name = "TERMINAL"
		self.definitions = [u'(of a disease or illness) leading gradually to death: ', u'A terminal patient is one who is seriously ill and will die soon.', u'extreme, when referring to something unpleasant or negative: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
