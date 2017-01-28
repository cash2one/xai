

#calss header
class _UNFLAGGING():
	def __init__(self,): 
		self.name = "UNFLAGGING"
		self.definitions = [u'If a quality, such as energy, interest, or enthusiasm, is unflagging, it never becomes weaker: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
