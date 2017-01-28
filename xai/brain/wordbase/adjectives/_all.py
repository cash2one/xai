

#calss header
class _ALL():
	def __init__(self,): 
		self.name = "ALL"
		self.definitions = [u'every one (of), or the complete amount or number (of), or the whole (of): ', u'considering all the different parts of the situation together: ', u'used when you make a comment or criticism, so that it seems less severe or is less likely to offend someone: ', u'the only and small amount or number of something you have: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
