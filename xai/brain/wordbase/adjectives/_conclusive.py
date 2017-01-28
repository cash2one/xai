

#calss header
class _CONCLUSIVE():
	def __init__(self,): 
		self.name = "CONCLUSIVE"
		self.definitions = [u'proving that something is true, or ending any doubt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
