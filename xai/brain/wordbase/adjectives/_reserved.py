

#calss header
class _RESERVED():
	def __init__(self,): 
		self.name = "RESERVED"
		self.definitions = [u'Reserved people do not often talk about or show their feelings or thoughts: ', u'Reserved tickets, seats, etc. are ones that you have arranged to be kept for you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
