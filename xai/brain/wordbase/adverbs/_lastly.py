

#calss header
class _LASTLY():
	def __init__(self,): 
		self.name = "LASTLY"
		self.definitions = [u'used to show when something comes after all the other things in a list: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
