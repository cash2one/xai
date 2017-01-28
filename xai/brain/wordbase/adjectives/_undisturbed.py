

#calss header
class _UNDISTURBED():
	def __init__(self,): 
		self.name = "UNDISTURBED"
		self.definitions = [u'not interrupted or changed in any way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
