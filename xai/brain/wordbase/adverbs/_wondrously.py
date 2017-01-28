

#calss header
class _WONDROUSLY():
	def __init__(self,): 
		self.name = "WONDROUSLY"
		self.definitions = [u'extremely, used to emphasize an approving description']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
