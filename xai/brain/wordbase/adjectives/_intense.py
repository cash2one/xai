

#calss header
class _INTENSE():
	def __init__(self,): 
		self.name = "INTENSE"
		self.definitions = [u'extreme and forceful or (of a feeling) very strong: ', u'Intense people are very serious, and usually have strong emotions or opinions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
