

#calss header
class _CONGESTIVE():
	def __init__(self,): 
		self.name = "CONGESTIVE"
		self.definitions = [u'involving or producing too much blood or other liquid in an organ: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
