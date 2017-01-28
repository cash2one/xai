

#calss header
class _AESTHETIC():
	def __init__(self,): 
		self.name = "AESTHETIC"
		self.definitions = [u'relating to the enjoyment or study of beauty: ', u'An aesthetic object or a work of art is one that shows great beauty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
