

#calss header
class _OUTSIDE():
	def __init__(self,): 
		self.name = "OUTSIDE"
		self.definitions = [u'not inside a building: ', u'coming from another place or organization: ', u'a phone call or connection going outside the place where you are', u'the most that would be accepted or possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
