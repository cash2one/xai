

#calss header
class _CHEEKY():
	def __init__(self,): 
		self.name = "CHEEKY"
		self.definitions = [u'slightly rude or showing no respect, but often in a funny way: ', u'used to describe something that you eat, drink, or do, especially when this is done quickly, without planning, or when you should not really do it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
