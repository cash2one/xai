

#calss header
class _PIED():
	def __init__(self,): 
		self.name = "PIED"
		self.definitions = [u'(used especially in the names of birds) having fur or feathers of two or more colours, usually black and white: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
