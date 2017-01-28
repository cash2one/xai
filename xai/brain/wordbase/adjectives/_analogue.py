

#calss header
class _ANALOGUE():
	def __init__(self,): 
		self.name = "ANALOGUE"
		self.definitions = [u'An analogue recording is one that is made by changing the sound waves into electrical signals of the same type.', u'a clock/watch that shows the time using numbers around the edge and hands that point to the numbers']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
