

#calss header
class _PLIABLE():
	def __init__(self,): 
		self.name = "PLIABLE"
		self.definitions = [u'A pliable substance bends easily without breaking or cracking: ', u'A pliable person is easily influenced and controlled by other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
