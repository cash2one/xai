

#calss header
class _DIM():
	def __init__(self,): 
		self.name = "DIM"
		self.definitions = [u'not giving or having much light: ', u'If your eyes are dim, you cannot see very well.', u'something that you remember slightly, but not very well: ', u'not very clever: ', u'not likely to succeed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
