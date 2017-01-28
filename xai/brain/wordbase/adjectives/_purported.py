

#calss header
class _PURPORTED():
	def __init__(self,): 
		self.name = "PURPORTED"
		self.definitions = [u'that has been stated to be true or to have happened, although this may not be the case: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
