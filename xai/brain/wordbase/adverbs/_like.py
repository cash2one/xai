

#calss header
class _LIKE():
	def __init__(self,): 
		self.name = "LIKE"
		self.definitions = [u'used before you describe how you were feeling or what you said when something happened to you: ', u'used in conversation as a pause or to emphasize an adjective: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
