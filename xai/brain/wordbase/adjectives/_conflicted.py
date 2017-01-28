

#calss header
class _CONFLICTED():
	def __init__(self,): 
		self.name = "CONFLICTED"
		self.definitions = [u'confused or worried because you cannot choose between very different ideas, feelings, or beliefs, and do not know what to do or believe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
