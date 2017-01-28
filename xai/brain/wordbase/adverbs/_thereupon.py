

#calss header
class _THEREUPON():
	def __init__(self,): 
		self.name = "THEREUPON"
		self.definitions = [u'immediately after something that is mentioned: ', u'on the thing that has been mentioned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
