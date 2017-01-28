

#calss header
class _INTERESTING():
	def __init__(self,): 
		self.name = "INTERESTING"
		self.definitions = [u'Someone or something that is interesting keeps your attention because he, she, or it is unusual, exciting, or has a lot of ideas: ', u'strange or different: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
