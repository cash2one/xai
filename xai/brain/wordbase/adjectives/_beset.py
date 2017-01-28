

#calss header
class _BESET():
	def __init__(self,): 
		self.name = "BESET"
		self.definitions = [u'having a lot of trouble with something, or having to deal with a lot of something that causes problems: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
