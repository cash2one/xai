

#calss header
class _UNEASY():
	def __init__(self,): 
		self.name = "UNEASY"
		self.definitions = [u'slightly worried or uncomfortable about a particular situation: ', u'used to describe a situation or condition that makes people slightly worried, often because it may not continue successfully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
