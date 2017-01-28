

#calss header
class _MEANWHILE():
	def __init__(self,): 
		self.name = "MEANWHILE"
		self.definitions = [u'until something expected happens, or while something else is happening: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
