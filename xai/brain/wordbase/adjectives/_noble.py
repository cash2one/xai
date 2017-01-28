

#calss header
class _NOBLE():
	def __init__(self,): 
		self.name = "NOBLE"
		self.definitions = [u'moral in an honest, brave, and kind way: ', u'belonging to a high social rank in a society, especially by birth: ', u'causing admiration because of a particular appearance or quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
