

#calss header
class _EXECUTIVE():
	def __init__(self,): 
		self.name = "EXECUTIVE"
		self.definitions = [u'relating to making decisions and managing businesses, or suitable for people with important jobs in business: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
