

#calss header
class _GERMANIC():
	def __init__(self,): 
		self.name = "GERMANIC"
		self.definitions = [u'typical of German people or things: ', u'belonging or relating to the group of languages that includes German, English, and Swedish: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
