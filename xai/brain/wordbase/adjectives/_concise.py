

#calss header
class _CONCISE():
	def __init__(self,): 
		self.name = "CONCISE"
		self.definitions = [u'short and clear, expressing what needs to be said without unnecessary words: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
