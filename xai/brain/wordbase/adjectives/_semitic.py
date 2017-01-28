

#calss header
class _SEMITIC():
	def __init__(self,): 
		self.name = "SEMITIC"
		self.definitions = [u'relating to the race of people that includes Arabs and Jews, or to their languages: ', u'Jewish', u'used to refer to races such as the Babylonians and Phoenicians that existed in ancient times']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
