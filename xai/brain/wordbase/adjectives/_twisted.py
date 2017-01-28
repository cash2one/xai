

#calss header
class _TWISTED():
	def __init__(self,): 
		self.name = "TWISTED"
		self.definitions = [u'bent so that the original shape is changed or destroyed: ', u'injured slightly by being bent: ', u'strange and slightly unpleasant or cruel: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
