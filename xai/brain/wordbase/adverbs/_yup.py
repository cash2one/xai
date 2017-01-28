

#calss header
class _YUP():
	def __init__(self,): 
		self.name = "YUP"
		self.definitions = [u'(spelled the way it is spoken) yes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
