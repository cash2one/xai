

#calss header
class _GREEN():
	def __init__(self,): 
		self.name = "GREEN"
		self.definitions = [u'of a colour between blue and yellow; of the colour of grass: ', u'relating to the protection of the environment: ', u'to do more to protect nature and the environment: ', u'covered with grass, trees, and other plants: ', u'(especially of fruit) not ready to eat, or (of wood) not dry enough to use: ', u'not experienced or trained: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
