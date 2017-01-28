

#calss header
class _PLIANT():
	def __init__(self,): 
		self.name = "PLIANT"
		self.definitions = [u'Pliant people are easily influenced or controlled by other people: ', u'being able and willing to accept change or new ideas: ', u'able to bend easily without breaking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
