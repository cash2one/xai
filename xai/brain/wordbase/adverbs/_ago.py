

#calss header
class _AGO():
	def __init__(self,): 
		self.name = "AGO"
		self.definitions = [u'back in time from the present: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
