

#calss header
class _INLINE():
	def __init__(self,): 
		self.name = "INLINE"
		self.definitions = [u'relating to or using inline skates: ', u'included as part of the main text on a page, rather than in a separate section: ', u'with parts arranged in a line: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
