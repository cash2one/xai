

#calss header
class _MISTY():
	def __init__(self,): 
		self.name = "MISTY"
		self.definitions = [u'If the weather is misty, there is mist in the air that makes it difficult to see into the distance: ', u'used to describe glass or a similar surface that is covered with a mist that makes it difficult to see through: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
