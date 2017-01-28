

#calss header
class _BITTER():
	def __init__(self,): 
		self.name = "BITTER"
		self.definitions = [u'Someone who is bitter is angry and unhappy because they cannot forget bad things that happened in the past: ', u'A bitter experience causes deep pain or anger: ', u'expressing a lot of hate and anger: ', u'with an unpleasantly sharp taste: ', u'Bitter weather is extremely cold, especially in a way that causes physical pain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
