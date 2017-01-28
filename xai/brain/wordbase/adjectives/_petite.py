

#calss header
class _PETITE():
	def __init__(self,): 
		self.name = "PETITE"
		self.definitions = [u'If a woman or girl is petite, she is small and thin in an attractive way: ', u'of a clothing size that is for small women']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
