

#calss header
class _ONWARD():
	def __init__(self,): 
		self.name = "ONWARD"
		self.definitions = [u'moving forward to a later time or a more distant (= farther away) place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
