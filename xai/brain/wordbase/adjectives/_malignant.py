

#calss header
class _MALIGNANT():
	def __init__(self,): 
		self.name = "MALIGNANT"
		self.definitions = [u'A malignant disease or growth is likely to get worse and lead to death: ', u'having a strong wish to do harm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
