

#calss header
class _JOCOSE():
	def __init__(self,): 
		self.name = "JOCOSE"
		self.definitions = [u'humorous or liking to play: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
