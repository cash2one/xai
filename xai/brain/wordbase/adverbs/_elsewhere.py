

#calss header
class _ELSEWHERE():
	def __init__(self,): 
		self.name = "ELSEWHERE"
		self.definitions = [u'at, in, from, or to another place or other places; anywhere or somewhere else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
