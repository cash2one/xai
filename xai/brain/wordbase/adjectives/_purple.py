

#calss header
class _PURPLE():
	def __init__(self,): 
		self.name = "PURPLE"
		self.definitions = [u'of a dark reddish-blue colour: ', u'dark red in the face because of anger', u'used to describe a piece of writing that is complicated or sounds false because the writer has tried too hard to make the style interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
