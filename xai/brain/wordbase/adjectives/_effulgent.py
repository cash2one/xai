

#calss header
class _EFFULGENT():
	def __init__(self,): 
		self.name = "EFFULGENT"
		self.definitions = [u'shining brightly: ', u'looking very beautiful or full of goodness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
