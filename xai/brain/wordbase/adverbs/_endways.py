

#calss header
class _ENDWAYS():
	def __init__(self,): 
		self.name = "ENDWAYS"
		self.definitions = [u'with the end, rather than the side, facing or touching: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
