

#calss header
class _ENTITLED():
	def __init__(self,): 
		self.name = "ENTITLED"
		self.definitions = [u'feeling that you have the right to do or have what you want without having to work for it or deserve it, just because of who you are: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
