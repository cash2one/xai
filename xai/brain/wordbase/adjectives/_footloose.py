

#calss header
class _FOOTLOOSE():
	def __init__(self,): 
		self.name = "FOOTLOOSE"
		self.definitions = [u'free to do what you like and go where you like because you have no responsibilities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
