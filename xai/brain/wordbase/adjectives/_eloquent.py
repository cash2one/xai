

#calss header
class _ELOQUENT():
	def __init__(self,): 
		self.name = "ELOQUENT"
		self.definitions = [u'giving a clear, strong message: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
