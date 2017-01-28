

#calss header
class _UNOBTRUSIVE():
	def __init__(self,): 
		self.name = "UNOBTRUSIVE"
		self.definitions = [u'not noticeable; seeming to fit in well with the things around: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
