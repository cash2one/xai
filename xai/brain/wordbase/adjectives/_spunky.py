

#calss header
class _SPUNKY():
	def __init__(self,): 
		self.name = "SPUNKY"
		self.definitions = [u'brave and determined', u'used to describe a man who is sexually attractive']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
