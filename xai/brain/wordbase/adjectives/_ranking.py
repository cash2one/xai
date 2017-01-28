

#calss header
class _RANKING():
	def __init__(self,): 
		self.name = "RANKING"
		self.definitions = [u'being the officer of highest rank present at a particular time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
