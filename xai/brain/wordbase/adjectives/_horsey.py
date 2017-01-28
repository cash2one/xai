

#calss header
class _HORSEY():
	def __init__(self,): 
		self.name = "HORSEY"
		self.definitions = [u'liking horses and being involved with them', u'looking like a horse, usually in a way that is not attractive']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
