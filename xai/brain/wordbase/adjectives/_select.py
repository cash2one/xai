

#calss header
class _SELECT():
	def __init__(self,): 
		self.name = "SELECT"
		self.definitions = [u'of only the best type or highest quality, and usually small in size or amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
