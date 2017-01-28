

#calss header
class _SHAVEN():
	def __init__(self,): 
		self.name = "SHAVEN"
		self.definitions = [u'with the hair removed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
