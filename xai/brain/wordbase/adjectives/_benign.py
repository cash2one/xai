

#calss header
class _BENIGN():
	def __init__(self,): 
		self.name = "BENIGN"
		self.definitions = [u'pleasant and kind: ', u'A benigntumour is not likely to cause death: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
