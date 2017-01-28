

#calss header
class _PATENT():
	def __init__(self,): 
		self.name = "PATENT"
		self.definitions = [u'very obvious: ', u'A patent invention is protected by law so that only particular people or companies have the right to make or sell it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
