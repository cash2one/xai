

#calss header
class _PREMATURE():
	def __init__(self,): 
		self.name = "PREMATURE"
		self.definitions = [u'happening or done too soon, especially before the natural or suitable time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
