

#calss header
class _INDIGENOUS():
	def __init__(self,): 
		self.name = "INDIGENOUS"
		self.definitions = [u'naturally existing in a place or country rather than arriving from another place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
