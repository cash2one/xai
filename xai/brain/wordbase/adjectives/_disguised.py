

#calss header
class _DISGUISED():
	def __init__(self,): 
		self.name = "DISGUISED"
		self.definitions = [u'having an appearance that hides the true form: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
