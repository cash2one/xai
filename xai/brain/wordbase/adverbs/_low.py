

#calss header
class _LOW():
	def __init__(self,): 
		self.name = "LOW"
		self.definitions = [u'close to the ground or the bottom of something: ', u'at or to a low level: ', u'to have nearly finished a supply of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
