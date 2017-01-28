

#calss header
class _SQUALID():
	def __init__(self,): 
		self.name = "SQUALID"
		self.definitions = [u'(of places) extremely dirty and unpleasant, often because of lack of money: ', u'(of situations and activities) not moral; involving sex and drugs, etc. in an unpleasant way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
