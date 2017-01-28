

#calss header
class _REPEATED():
	def __init__(self,): 
		self.name = "REPEATED"
		self.definitions = [u'happening again and again: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
