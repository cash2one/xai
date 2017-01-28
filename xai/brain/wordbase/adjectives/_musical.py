

#calss header
class _MUSICAL():
	def __init__(self,): 
		self.name = "MUSICAL"
		self.definitions = [u'related to or connected with music: ', u'If you are musical, you have a skill in or a great liking for music: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
