

#calss header
class _PICTURESQUE():
	def __init__(self,): 
		self.name = "PICTURESQUE"
		self.definitions = [u'(especially of a place) attractive in appearance, especially in an old-fashioned way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
