

#calss header
class _DUMBFOUNDED():
	def __init__(self,): 
		self.name = "DUMBFOUNDED"
		self.definitions = [u'so shocked that you cannot speak: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
