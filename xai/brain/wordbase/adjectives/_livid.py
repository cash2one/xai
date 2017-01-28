

#calss header
class _LIVID():
	def __init__(self,): 
		self.name = "LIVID"
		self.definitions = [u'extremely angry: ', u'(especially of marks on the skin) of an unpleasant purple or dark blue colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
