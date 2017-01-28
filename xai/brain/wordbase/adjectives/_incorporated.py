

#calss header
class _INCORPORATED():
	def __init__(self,): 
		self.name = "INCORPORATED"
		self.definitions = [u'used after the name of a company that is a corporation (= a company or goup of companies controlled as one organization): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
