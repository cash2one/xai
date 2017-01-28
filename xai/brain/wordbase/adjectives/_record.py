

#calss header
class _RECORD():
	def __init__(self,): 
		self.name = "RECORD"
		self.definitions = [u'at a higher level than ever achieved before: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
