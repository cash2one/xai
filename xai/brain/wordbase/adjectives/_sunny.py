

#calss header
class _SUNNY():
	def __init__(self,): 
		self.name = "SUNNY"
		self.definitions = [u'bright because of light from the sun: ', u'A sunny person is usually happy and relaxed and does not usually get worried or angry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
