

#calss header
class _FRIGID():
	def __init__(self,): 
		self.name = "FRIGID"
		self.definitions = [u'(of a woman) having difficulty in becoming sexually excited', u'unfriendly or very formal: ', u'(of weather conditions or the conditions in a room) extremely cold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
