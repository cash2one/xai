

#calss header
class _WIDOWED():
	def __init__(self,): 
		self.name = "WIDOWED"
		self.definitions = [u'used to describe a person whose husband or wife has died: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
