

#calss header
class _SATISFIED():
	def __init__(self,): 
		self.name = "SATISFIED"
		self.definitions = [u'pleased because you have got what you wanted, or because something has happened in the way that you wanted: ', u'If you are satisfied that something is true, you believe it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
