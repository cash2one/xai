

#calss header
class _DESIGNING():
	def __init__(self,): 
		self.name = "DESIGNING"
		self.definitions = [u'used to describe someone who tries to get what they want, usually dishonestly']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
