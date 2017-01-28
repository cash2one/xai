

#calss header
class _PREPAY():
	def __init__(self,): 
		self.name = "PREPAY"
		self.definitions = [u'used to refer to a mobile phone that you must pay to use before you can use it']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
