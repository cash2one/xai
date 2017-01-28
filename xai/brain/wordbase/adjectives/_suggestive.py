

#calss header
class _SUGGESTIVE():
	def __init__(self,): 
		self.name = "SUGGESTIVE"
		self.definitions = [u'often used to describe something that makes people think about sex: ', u'If something is suggestive of something else, it makes you think about it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
