

#calss header
class _DAUNTING():
	def __init__(self,): 
		self.name = "DAUNTING"
		self.definitions = [u'making you feel slightly frightened or worried about your ability to achieve something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
