

#calss header
class _SPANKING():
	def __init__(self,): 
		self.name = "SPANKING"
		self.definitions = [u'(used with some adjectives) very, completely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
