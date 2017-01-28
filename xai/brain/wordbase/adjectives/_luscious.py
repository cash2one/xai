

#calss header
class _LUSCIOUS():
	def __init__(self,): 
		self.name = "LUSCIOUS"
		self.definitions = [u'having a pleasant sweet taste or containing a lot of juice: ', u'(of a woman) very sexually attractive: ', u'(of an area of countryside) very green and attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
