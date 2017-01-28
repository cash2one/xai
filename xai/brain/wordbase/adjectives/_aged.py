

#calss header
class _AGED():
	def __init__(self,): 
		self.name = "AGED"
		self.definitions = [u'of the age of: ', u'old: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
