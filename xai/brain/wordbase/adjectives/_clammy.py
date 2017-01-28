

#calss header
class _CLAMMY():
	def __init__(self,): 
		self.name = "CLAMMY"
		self.definitions = [u'sticky and slightly wet in an unpleasant way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
