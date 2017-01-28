

#calss header
class _TIMID():
	def __init__(self,): 
		self.name = "TIMID"
		self.definitions = [u'shy and nervous; without much confidence; easily frightened: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
